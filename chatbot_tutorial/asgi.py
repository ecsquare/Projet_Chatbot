"""
ASGI config for chatbot_website project.
Used for WebSockets
"""

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot_tutorial.settings")
channel_layer = channels.asgi.get_channel_layer()