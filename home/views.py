from django.shortcuts import render ,  get_object_or_404
from django.views.decorators.http import condition
from .conditionalViewSynchronizer import last_modified_func
from .appInstanceData import AppInstance
from django.views.decorators.cache import cache_page
from django.conf import settings



@condition(last_modified_func=last_modified_func)
@cache_page(60 * 5)  # 5 minute cache
def home_page(request):
    # Get the single AppInstance row
    # Using your own get_instance() classmethod → very clean
    instance = get_object_or_404(
        AppInstance,
        id=settings.APP_INSTANCE_ID,
        is_active=True
    )
    
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
    
    return render(request, 'index.html', context)