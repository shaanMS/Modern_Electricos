import uuid
import hashlib
from django.db import models
from django.utils import timezone
from django.contrib.postgres.indexes import GinIndex
from django.db.models import Q


class Enquiry(models.Model):

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    BUDGET_CHOICES = [
        ("under500", "Under 500"),
        ("500-1000", "500 - 1000"),
        ("1000-5000", "1000 - 5000"),
        ("5000-10000", "5000 - 10000"),
        ("over10000", "Over 10000"),
    ]

    # Primary
    id = models.BigAutoField(primary_key=True)

    # Public UUID (safe to expose)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)

    # Basic info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=20, db_index=True)

    address = models.TextField(blank=True, null=True)

    service_required = models.JSONField()  # multi select support

    project_details = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="low",
        db_index=True
    )

    preferred_date = models.DateField(null=True, blank=True)

    budget = models.CharField(
        max_length=20,
        choices=BUDGET_CHOICES,
        blank=True,
        null=True
    )

    # Security tracking
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    referer = models.TextField(null=True, blank=True)

    # Fingerprint hash
    request_hash = models.CharField(max_length=64, db_index=True)

    # Instance ID (cookie token bind)
    instance_id = models.UUIDField(null=True, blank=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    is_processed = models.BooleanField(default=False, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=["email", "created_at"]),
            models.Index(fields=["phone", "created_at"]),
            models.Index(fields=["priority", "is_processed"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["request_hash"],
                name="unique_request_hash"
            )
        ]

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
