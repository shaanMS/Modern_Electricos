from django.urls import path
from .views import home_page , instance_page

urlpatterns = [
    path("", home_page, name="home"),
    path("franchise/<uuid:franchise_uuid>/", instance_page, name="home"),
    
] 
