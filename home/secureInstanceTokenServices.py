# security.py

import base64
import hmac
import hashlib
import time
from django.conf import settings
from django.utils.crypto import constant_time_compare


# function to send timestamp and to token generation for http only cookie for instanceUUID verification  


SEPARATOR = "|"


def create_instance_token(instance_uuid):
    #timestamp = str(int(time.time()))  abhi bina timestamp k hi
    # or apply timestamp for post latest page not on old page 
    timestamp = str(int(time.time()))
    payload = f"{instance_uuid}{SEPARATOR}{timestamp}"

    signature = hmac.new(
        settings.SECRET_KEY.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

    final_token = f"{payload}{SEPARATOR}{signature}"

    return base64.urlsafe_b64encode(final_token.encode()).decode()











# function to compare time and life of token and page  and to decrypt


def verify_instance_token(token: str, max_age_seconds=86400):
    try:
        decoded = base64.urlsafe_b64decode(token).decode()
        instance_uuid, timestamp, signature = decoded.split(SEPARATOR)

        payload = f"{instance_uuid}{SEPARATOR}{timestamp}"

        expected_signature = hmac.new(
            settings.SECRET_KEY.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()

        if not constant_time_compare(signature, expected_signature):
            return None

        # Expiry check
        if int(time.time()) - int(timestamp) > max_age_seconds:
            return None

        return instance_uuid

    except Exception:
        return None