# from django.views.decorators.http import require_POST
# from django.http import JsonResponse
# from django.core.cache import cache
# from django.utils import timezone
# from django.db import transaction
# from .hashToken import generate_request_hash
# from .models import Enquiry




# @require_POST
# def submit_enquiry(request):

#     ip = request.META.get("REMOTE_ADDR")
#     user_agent = request.META.get("HTTP_USER_AGENT")
#     referer = request.META.get("HTTP_REFERER")

#     # Rate limit (per IP 5 requests / 5 minutes)
#     rate_key = f"enquiry_rate_{ip}"
#     count = cache.get(rate_key, 0)

#     if count >= 5:
#         return JsonResponse({"error": "Too many requests"}, status=429)

#     cache.set(rate_key, count + 1, timeout=300)

#     data = request.POST

#     request_hash = generate_request_hash(data, ip, user_agent)

#     if Enquiry.objects.filter(request_hash=request_hash).exists():
#         return JsonResponse({"error": "Duplicate submission"}, status=400)

#     with transaction.atomic():
#         enquiry = Enquiry.objects.create(
#             first_name=data.get("first_name"),
#             last_name=data.get("last_name"),
#             email=data.get("email"),
#             phone=data.get("phone"),
#             address=data.get("address"),
#             service_required=data.getlist("service_required"),
#             project_details=data.get("project_details"),
#             priority=data.get("priority"),
#             preferred_date=data.get("preferred_date") or None,
#             budget=data.get("budget"),
#             ip_address=ip,
#             user_agent=user_agent,
#             referer=referer,
#             request_hash=request_hash,
#         )

#     return JsonResponse({"success": True, "uuid": str(enquiry.uuid)})





















# views.py

import json
import hashlib
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from .models import Enquiry


@require_POST
@csrf_protect
def enquiry_create_view(request):
    try:
        # ----------------------------
        # Basic Required Fields
        # ----------------------------
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        phone = request.POST.get("phone", "").strip()
        project_details = request.POST.get("project_details", "").strip()
        priority = request.POST.get("priority", "low")
        preferred_date = request.POST.get("preferred_date") or None
        budget = request.POST.get("budget") or None
        address = request.POST.get("address") or None

        service_required = request.POST.getlist("service_required")

        # ----------------------------
        # Manual Validation
        # ----------------------------

        errors = {}

        if not first_name:
            errors["first_name"] = "First name is required"

        if not last_name:
            errors["last_name"] = "Last name is required"

        if not email:
            errors["email"] = "Email is required"
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors["email"] = "Invalid email format"

        if not phone:
            errors["phone"] = "Phone is required"

        if not project_details:
            errors["project_details"] = "Project details are required"

        if not service_required:
            errors["service_required"] = "Select at least one service"

        if errors:
            return JsonResponse(
                {"success": False, "errors": errors},
                status=400
            )

        # ----------------------------
        # Security Metadata
        # ----------------------------

        ip_address = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT")
        referer = request.META.get("HTTP_REFERER")

        # instance_id from secure cookie
        instance_id = request.COOKIES.get("app_instance")

        # ----------------------------
        # Fingerprint Hash
        # ----------------------------

        hash_input = f"{email}{phone}{project_details}{ip_address}"
        request_hash = hashlib.sha256(hash_input.encode()).hexdigest()

        # ----------------------------
        # DB Insert (Atomic)
        # ----------------------------

        with transaction.atomic():
            enquiry = Enquiry.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                service_required=service_required,
                project_details=project_details,
                priority=priority,
                preferred_date=preferred_date,
                budget=budget,
                ip_address=ip_address,
                user_agent=user_agent,
                referer=referer,
                request_hash=request_hash,
                instance_id=instance_id,
            )

        return JsonResponse(
            {
                "success": True,
                "message": "Enquiry submitted successfully",
                "uuid": str(enquiry.uuid),
            },
            status=201
        )

    except IntegrityError:
        return JsonResponse(
            {
                "success": False,
                "error": "Duplicate enquiry detected."
            },
            status=409
        )

    except Exception as e:
        return JsonResponse(
            {
                "success": False,
                "error": "Internal server error"
            },
            status=500
        )
