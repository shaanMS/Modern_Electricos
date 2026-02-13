from home.models import AppInstance
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import AppInstance
import random
import asyncio
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync



@sync_to_async(thread_sensitive=True)
def get_instance():
    return get_object_or_404(        AppInstance,
        id=settings.APP_INSTANCE_ID,
        is_active=True
    )