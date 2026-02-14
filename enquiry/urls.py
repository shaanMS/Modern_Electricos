# apps/enquiry/urls.py

from django.urls import path
from .views import enquiry_create_view

app_name = "enquiry"

urlpatterns = [
    path(
        "form/<slug:form_slug>/project/<slug:project_slug>/enquiry/submit/",
        enquiry_create_view,
        name="submit",
    ),
]
