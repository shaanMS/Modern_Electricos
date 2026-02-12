from home.models import AppInstance
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import AppInstance
import random


def last_modified_func(request, *args, **kwargs):
    instance = get_object_or_404(
        AppInstance,
        id=settings.APP_INSTANCE_ID,
        is_active=True
    )
    print('',random.randint(1,5))
    if instance:
        return instance.last_modified
    return None
