from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField 
from django.contrib.postgres.fields import DateRangeField, DateTimeRangeField, IntegerRangeField, DecimalRangeField
from django.utils import timezone
import uuid
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from django.db.models import JSONField


class AppInstance(models.Model):
    """
    SINGLE MODEL - Sirf UI ke saare static data ke liye
    All PostgreSQL data types included
    """
    
    # ===== 1. PRIMARY KEY =====
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="UUID primary key"
    )
    
    # ===== 2. CHAR FIELDS =====
    title = models.CharField(
        max_length=200,
        default='PowerPro Electrical',
        help_text="Company title - CharField"
    )
    
    tagline = models.CharField(
        max_length=200,
        default='Professional Electrical Solutions',
        help_text="Company tagline - CharField"
    )
    
    contact = models.CharField(
        max_length=50,
        default='1-800-555-3782',
        help_text="Contact number - CharField"
    )
    
    email = models.EmailField(
        max_length=100,
        default='info@powerproelectrical.com',
        help_text="Email address - EmailField"
    )
    
    reviews_and_count = models.CharField(
        max_length=50,
        default='4.8/5 (247 reviews)',
        help_text="Reviews text - CharField"
    )
    
    hero_subtitle = models.CharField(
        max_length=500,
        default='Licensed & insured electrical services with 24/7 emergency support. Serving residential and commercial clients since 2005.',
        help_text="Hero subtitle - CharField"
    )
    
    # ===== 3. TEXT FIELDS =====
    about_text = models.TextField(
        blank=True,
        null=True,
        help_text="About company - TextField"
    )
    
    footer_text = models.TextField(
        blank=True,
        null=True,
        help_text="Footer text - TextField"
    )
    
    # ===== 4. INTEGER FIELDS =====
    project_complete_count = models.IntegerField(
        default=2473,
        help_text="Projects completed count - IntegerField"
    )
    
    service_years = models.PositiveIntegerField(
        default=18,
        help_text="Years of service - PositiveIntegerField"
    )
    
    employees_count = models.SmallIntegerField(
        default=50,
        help_text="Number of employees - SmallIntegerField"
    )
    
    office_locations = models.BigIntegerField(
        default=5,
        help_text="Number of office locations - BigIntegerField"
    )
    
    # ===== 5. DECIMAL FIELDS =====
    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=4.80,
        help_text="Average rating - DecimalField"
    )
    
    satisfaction_rate = models.FloatField(
        default=98.5,
        help_text="Customer satisfaction rate - FloatField"
    )
    
    # ===== 6. BOOLEAN FIELDS =====
    show_ad_section = models.BooleanField(
        default=True,
        help_text="Show/hide ad section - BooleanField"
    )
    
    is_emergency_available = models.BooleanField(
        default=True,
        help_text="Emergency service available - BooleanField"
    )
    
    is_licensed = models.BooleanField(
        default=True,
        help_text="Company licensed - BooleanField"
    )
    
    is_insured = models.BooleanField(
        default=True,
        help_text="Company insured - BooleanField"
    )
    
    # ===== 7. DATE/TIME FIELDS =====
    founded_date = models.DateField(
        default=timezone.now,
        help_text="Company founded date - DateField"
    )
    
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text="Last updated timestamp - DateTimeField"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Created timestamp - DateTimeField"
    )
    
    # ===== 8. JSON FIELD - PostgreSQL Specific =====
    company_info = JSONField(
        default=dict,
        help_text="Company info as JSONB - JSONField"
    )
    
    seo_settings = JSONField(
        default=dict,
        help_text="SEO settings as JSONB - JSONField"
    )
    
    theme_settings = JSONField(
        default=dict,
        help_text="Theme colors as JSONB - JSONField"
    )
    
    # ===== 9. ARRAY FIELD - PostgreSQL Specific =====
    ads = models.JSONField(default=list, blank=True)
    services_data = models.JSONField(default=list, blank=True)
    
    business_hours = ArrayField(
        models.CharField(max_length=100),
        default=list,
        help_text="Business hours array - ArrayField of CharField"
    )
    
    certifications = ArrayField(
        models.CharField(max_length=100),
        default=list,
        help_text="Certifications array - ArrayField"
    )
    
    payment_methods = ArrayField(
        models.CharField(max_length=50),
        default=list,
        help_text="Payment methods array - ArrayField"
    )
    
    service_areas = ArrayField(
        models.CharField(max_length=100),
        default=list,
        help_text="Service areas array - ArrayField"
    )
    
    # ===== 10. HSTORE FIELD - PostgreSQL Specific =====
    metadata = JSONField(
    default=dict,
    blank=True,
    help_text="Key-value metadata - JSONB"
)
    
    statistics = JSONField(
    default=dict,
    blank=True,
    help_text="Statistics key-value - JSONB"
)
    
    # ===== 11. RANGE FIELDS - PostgreSQL Specific =====
    active_period = DateRangeField(
        null=True,
        blank=True,
        help_text="Active date range - DateRangeField"
    )
    
    support_hours = DateTimeRangeField(
        null=True,
        blank=True,
        help_text="Support hours range - DateTimeRangeField"
    )
    
    employee_count_range = IntegerRangeField(
        null=True,
        blank=True,
        help_text="Employee count range - IntegerRangeField"
    )
    
    budget_range = DecimalRangeField(
        null=True,
        blank=True,
        help_text="Budget range - DecimalRangeField"
    )
    
    # ===== 12. URL FIELD =====
    website_url = models.URLField(
        max_length=500,
        blank=True,
        default='https://www.powerproelectrical.com',
        help_text="Website URL - URLField"
    )
    
    facebook_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Facebook URL - URLField"
    )
    
    instagram_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Instagram URL - URLField"
    )
    
    linkedin_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="LinkedIn URL - URLField"
    )
    
    # ===== 13. FILE/UPLOAD FIELDS =====
    logo = models.ImageField(
        upload_to='logos/',
        blank=True,
        null=True,
        help_text="Company logo - ImageField"
    )
    
    favicon = models.FileField(
        upload_to='favicon/',
        blank=True,
        null=True,
        help_text="Favicon - FileField"
    )
    
    # ===== 14. SLUG FIELD =====
    slug = models.SlugField(
        max_length=255,
        unique=True,
        default='powerpro-electrical',
        help_text="URL slug - SlugField"
    )
    
    # ===== 15. GENERIC IP ADDRESS =====
    last_modified_by_ip = models.GenericIPAddressField(
        blank=True,
        null=True,
        help_text="Last modified by IP - GenericIPAddressField"
    )
    
    # ===== 16. AUTO INCREMENT BIG INTEGER =====
    instance_version = models.BigIntegerField(
    default=1,
    unique=True,
    help_text="Instance version - BigIntegerField"
)
    
    is_active = models.BooleanField(default=False)

    last_modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'app_instance'
        verbose_name = 'App Instance'
        verbose_name_plural = 'App Instances'
        indexes = [
            models.Index(fields=['title', 'slug']),
            models.Index(fields=['-created_at']),
         # ⚡ JSONB GIN Indexes (Very Fast)
            GinIndex(fields=['company_info']),
            GinIndex(fields=['seo_settings']),
            GinIndex(fields=['theme_settings']),
            GinIndex(fields=['metadata'] ,name='metadata_gin_idx' ),
            GinIndex(fields=['statistics']),

]

    
    def __str__(self):
        return f"{self.title} - v{self.instance_version}"
    
    # def save(self, *args, **kwargs):
    #     # Ensure only one instance exists
    #     if not self.pk and AppInstance.objects.exists():
    #         # Copy data from existing instance
    #         existing = AppInstance.objects.first()
    #         self.pk = existing.pk
    #     super().save(*args, **kwargs)
    
    # @classmethod
    # def get_instance(cls):
    #     """Get or create the single app instance"""
    #     instance, created = cls.objects.get_or_create(
    #         defaults={
    #             'title': 'PowerPro Electrical',
    #             'tagline': 'Professional Electrical Solutions',
    #             'contact': '1-800-555-3782',
    #             'email': 'info@powerproelectrical.com',
    #             'hero_subtitle': 'Licensed & insured electrical services with 24/7 emergency support.',
    #         }
    #     )
        return instance