import os
from channels.asgi import get_channel_layer


PROJECT_NAME = os.environ.get("PROJECT_NAME")
PROJECT_SETTINGS = f"{PROJECT_NAME}.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", PROJECT_SETTINGS)
channel_layer = get_channel_layer()
