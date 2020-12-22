from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from .models import WebsocketToken

# class TokenAuthenticationMiddleware():
#     def __init__(self, app):
#         self.app = app
#
#     def __call__(self, scope):
#         return TokenAuthenticationMiddlewareInstance(scope, self)


class TokenAuthenticationMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        user = await self.get_user(scope)
        print("checking auth")
        if user:
            scope['user'] = user
            print("authed")
        return await self.app(scope, receive, send)

    @database_sync_to_async
    def get_user(self,scope):
        try:
            token = parse_qs(scope['query_string'].decode('utf8'))
            key=token['key'][0]
            print(token)
            try:
                token = WebsocketToken.objects.get(key=key)
                print(token)
                return token.user
                # print(token)
                # if token:
                #     return token.user
                #
                # print(token.is_expired())
            except WebsocketToken.DoesNotExist:
                return None
        except KeyError:
            return None
