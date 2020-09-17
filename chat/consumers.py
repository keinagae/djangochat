from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.layers import get_channel_layer
from .models import Conversion, Message
from .serializers import MessageSerializer


class ChatWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated:
            self.user = self.scope['url_route']['kwargs']['user']
            current_user = self.scope['user']
            self.conversion = await database_sync_to_async(self.get_room)(current_user, self.user)
            self.room_name = f'conversion_{self.conversion.id}'
            await self.channel_layer.group_add(
                self.room_name,
                self.channel_name
            )
            await self.accept()
        else:
             await self.close(400)

    @staticmethod
    def get_room(user, user_id):
        try:
            user2 = get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExists:
            return None
        conversion = Conversion.objects.get_room(user, user2)
        return conversion
    @database_sync_to_async
    def save_message(self, message):
        return Message.objects.create(conversion=self.conversion, message=message, user=self.scope['user'])

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        # message = content['message']
        message = await self.save_message(content['message'])
        response = await self.serialize(message)
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "chat_message",
                'message': response
            }
        )
        await self.notify_others()


    async def notify_others(self):
        users=await self.get_other_users()
        for user in users:
            print(f"user__{user.pk}")
            await self.channel_layer.group_send(
                f"user__{user.pk}",
                {
                    'type': 'message_received',
                    'message': 'dfsfsdf'
                }
            )
    @database_sync_to_async
    def get_other_users(self):
        return list(self.conversion.participants.filter(id=self.scope['user'].pk))
    @database_sync_to_async
    def serialize(self, data):
        return MessageSerializer(data).data

    async def chat_message(self, event):
        message = event['message']
        await self.send_json(message)


class ChatNotify(AsyncJsonWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated:
            user = self.scope['user']
            print(f"user__{user.pk}")
            self.room_name = f"user__{user.pk}"
            self.channel_layer.group_add(self.room_name, self.channel_name)
            await self.accept()
        else:
            await self.close(400)

    async def disconnect(self):
        self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def message_received(self,event):
        message = event['message']
        print("dfsdfsdfdsf")
        await self.send_json(message)

