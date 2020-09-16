from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

import chat.routing
from chat.middlewares import TokenAuthenticationMiddleware

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': TokenAuthenticationMiddleware(
        AuthMiddlewareStack(
            URLRouter([
                path("ws", URLRouter([
                    path('chat', URLRouter(
                        chat.routing.urlpatterns
                    ))
                ]))
            ])
        )
    ),
})
