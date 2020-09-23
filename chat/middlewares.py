from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from .models import WebsocketToken

class TokenAuthenticationMiddleware():
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return TokenAuthenticationMiddlewareInstance(scope, self)


class TokenAuthenticationMiddlewareInstance():
    def __init__(self, scope, middleware):
        self.scope = dict(scope)
        self.inner = middleware.inner

    async def __call__(self, receive, send):
        user = await self.get_user()
        if user:
            self.scope['user'] = user
        inner = self.inner(self.scope)
        return await inner(receive, send)

    @database_sync_to_async
    def get_user(self):
        try:
            token = parse_qs(self.scope['query_string'].decode('utf8'))
            key=token['key'][0]
            try:
                token = WebsocketToken.objects.get(key=key)
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
