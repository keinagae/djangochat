from channels.routing import ProtocolTypeRouter
from django.urls import re_path,path
from channels.auth import AuthMiddleware
from . import consumers
urlpatterns = [
    path('<int:user>/', consumers.ChatWebsocketConsumer.as_asgi()),
    path('notify',consumers.ChatNotify.as_asgi())
]