from django.shortcuts import render ,  get_object_or_404
from django.views.decorators.http import condition
from .conditionalViewSynchronizer import last_modified_func
from .appInstanceData import AppInstance
from django.views.decorators.cache import cache_page
from django.conf import settings
#from ratelimit.decorators import ratelimit
import logging
from django.http import HttpResponseForbidden
from django.http import JsonResponse ,HttpResponse
import asyncio
from django.core.signing import Signer
from django.http import StreamingHttpResponse
import asyncio
from .secureInstanceTokenServices import constant_time_compare ,create_instance_token
from django.views.decorators.csrf import ensure_csrf_cookie





logger = logging.getLogger(__name__)


@ensure_csrf_cookie
#@ratelimit(key='ip', rate='5/m', block=True)
@condition(last_modified_func=last_modified_func)
@cache_page(60 * 5)  # 5 minute cache  iski wajah se csrf stale ho rha hai to ab block level cache kar rhe hai template m 
def home_page(request):
    # Get the single AppInstance row
    # Using your own get_instance() classmethod → very clean
    instance = get_object_or_404(
        AppInstance,
        id=settings.APP_INSTANCE_ID,
        is_active=True
    )
    print('y home view m instance hai y pass hoga token gen k liye')
    print(instance  ,'   ye instance name hogya ! dekha kahli instance likhaha to __str__ call hua or uska return value yaani title return hogya  ')
    print(instance.id  ,'   ye instance id hogya')
    token = create_instance_token(instance.id)  # agar direct instance pass kiya to str callhokar return uska yaani title h chala jayega instance.id hamesha yaad rkho
    print(token,'   -     ------     y token hogya')
    # Prepare context with flattened + renamed fields
    # (matching the template variables you are already using)
    context = {
        # Basic company info
        'title': instance.title,
        'tagLine': instance.tagline,           # note: camelCase as in your template
        'contact': instance.contact,
        'email': instance.email,
        'heroSubtitle': instance.hero_subtitle,
        'reviewsAndCount': instance.reviews_and_count,
        
        # Stats / counters
        'projectCompleteCount': instance.project_complete_count,
        'serviceYears': instance.service_years,
        
        # Control flags
        'show_ad_section': instance.show_ad_section,
        
        # Arrays / JSON → pass directly (template will loop)
        'ads': instance.ads,                    # list of dicts → expected keys: image_url, link_url, alt_text
        'services_data': instance.services_data, # you can use this instead of hardcoded JS array later
        
        # Optional – if you want to show more later
        'about_text': instance.about_text,
        'business_hours': instance.business_hours,
        'certifications': instance.certifications,
        'service_areas': instance.service_areas,
        'payment_methods': instance.payment_methods,
        
        # You can add more fields gradually
    }
    
    
    response = render(request, "index.html" ,context)
    
    print(render  , '    --- y render ka obje hai   ',response)
    print('response set token ')
    response.set_cookie(
        key="app_instance",
        value=token,
        httponly=True,
     #   secure=True,       # enable in production
        
        samesite="Lax",
        max_age=86400
    )
    print("POST DATA:", request.POST)
    print("CSRF in POST:", request.POST.get("csrfmiddlewaretoken"))
    print("CSRF in META:", request.META.get("HTTP_X_CSRFTOKEN"))
    return response    #render(request, 'index.html', context)
















@ensure_csrf_cookie
#@ratelimit(key='ip', rate='5/m', block=True)
@condition(last_modified_func=last_modified_func)
@cache_page(60 * 5)  # 5 minute cache  iski wajah se csrf stale ho rha hai to ab block level cache kar rhe hai template m 

def instance_page(request, franchise_uuid):
 try: 
    # y kaam middleware level par bhi ho sakta hai yaani har request par generation and verification ho ta rahega custom midddleware se ok     
    
    print('i m in uuid ')   
        
        
    instance = AppInstance.objects.get(id=franchise_uuid)#, is_active=True) # y string hai
    # khali instance string hi hai 
    print('y home view m instance hai y pass hoga token gen k liye')
    token = create_instance_token(instance.id)   
    print('y token ban gaya hai    ',token)
    #return HttpResponse(f"Franchise: {franchise.title}")
    context = {
        # Basic company info
        'title  - Franchise Of Shakti Electricals': instance.title,
        'tagLine': instance.tagline,           # note: camelCase as in your template
        'contact': instance.contact,
        'email': instance.email,
        'heroSubtitle': instance.hero_subtitle,
        'reviewsAndCount': instance.reviews_and_count,
        
        # Stats / counters
        
        'projectCompleteCount': instance.project_complete_count,
        'serviceYears': instance.service_years,
        
        # Control flags
        'show_ad_section': instance.show_ad_section,
        
        # Arrays / JSON → pass directly (template will loop)
        'ads': instance.ads,                    # list of dicts → expected keys: image_url, link_url, alt_text
        'services_data': instance.services_data, # you can use this instead of hardcoded JS array later
        
        # Optional – if you want to show more later
        'about_text': instance.about_text,
        'business_hours': instance.business_hours,
        'certifications': instance.certifications,
        'service_areas': instance.service_areas,
        'payment_methods': instance.payment_methods,
        
        # You can add more fields gradually
    }
    
    #  return render(request, 'index.html', context)
    response = render(request, "index.html" ,context)
    print('response set token in franchise ')
    response.set_cookie(
        key="app_instance",
        value=token,
        httponly=True,
       # secure=True,       # enable in production
        samesite="Lax",
        max_age=86400
    )
    
    return response    #render(request, 'index.html', context)


 except AppInstance.DoesNotExist:
     logger.warning(f"Unauthorized access attempt by {request.user} for {franchise_uuid}")
     return HttpResponseForbidden("Access Denied",)















async def async_sse(request):
    async def event_stream():
        for i in range(5):
            yield f"data: {i}\n\n"
            await asyncio.sleep(1)
    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


