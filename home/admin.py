from django.contrib import admin
from .models import AppInstance
import json

@admin.register(AppInstance)
class AppInstanceAdmin(admin.ModelAdmin):
    list_display = ['title', 'tagline', 'instance_version', 'last_updated', 'show_ad_section']
    list_filter = ['show_ad_section', 'is_licensed', 'is_insured', 'created_at']
    search_fields = ['title', 'tagline', 'email', 'contact']
    readonly_fields = ['instance_version', 'created_at', 'last_updated']
    
    fieldsets = (
        ('🏢 COMPANY INFORMATION', {
            'fields': (
                'title', 'tagline', 'slug', 'logo', 'favicon',
                'contact', 'email', 'website_url',
                'facebook_url', 'instagram_url', 'linkedin_url'
            )
        }),
        
        ('📊 STATISTICS', {
            'fields': (
                'project_complete_count', 'service_years',
                'employees_count', 'office_locations',
                'average_rating', 'satisfaction_rate'
            )
        }),
        
        ('⚙️ SETTINGS', {
            'fields': (
                'show_ad_section', 'is_emergency_available',
                'is_licensed', 'is_insured'
            )
        }),
        
        ('📅 DATES', {
            'fields': (
                'founded_date', 'active_period', 'support_hours',
                'created_at', 'last_updated'
            )
        }),
        
        ('📦 JSON FIELDS', {
            'fields': (
                'company_info', 'seo_settings', 'theme_settings',
                'ads', 'services_data'
            ),
            'classes': ('collapse',),
        }),
        
        ('📋 ARRAY FIELDS', {
            'fields': (
                'business_hours', 'certifications',
                'payment_methods', 'service_areas'
            ),
            'classes': ('collapse',),
        }),
        
        ('🔧 POSTGRESQL SPECIFIC', {
            'fields': (
                'metadata', 'statistics',
                'employee_count_range', 'budget_range'
            ),
            'classes': ('collapse',),
        }),
        
        ('📝 TEXT CONTENT', {
            'fields': ('hero_subtitle', 'about_text', 'footer_text', 'reviews_and_count'),
            'classes': ('wide',),
        }),
    )