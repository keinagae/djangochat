from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from channels.layers import get_channel_layer

from user.models import UserStatusEnum
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
            # await self.channel_layer.group_add(f"user__{self.user}", self.channel_name)
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
        if content.get("action","")=="message":
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
        elif content.get("action","")=="start_typing":
            print("started_typing")
        elif content.get("action","")=="stop_typing":
            print("stop_typing")


    async def notify_others(self):
        users=await self.get_other_users()
        await notify(users)
        
            
    @database_sync_to_async
    def get_other_users(self):
        return list(self.conversion.participants.all())
    @database_sync_to_async
    def serialize(self, data):
        return MessageSerializer(data).data


    async def chat_message(self, event):
        message = event['message']

        await self.send_json({
            'action':'message',
            'data':message
        })


class ChatNotify(AsyncJsonWebsocketConsumer):

    async def connect(self):
        if self.scope['user'].is_authenticated:
            await self.accept()
            self.user = self.scope['user']
            self.room_name = f"user__{self.user.pk}"
            await self.channel_layer.group_add(self.room_name, self.channel_name)
            await  self.set_online()
            print(f"user {self.user.username} connected  to {self.room_name} notifications")
        else:
            await self.close(400)

    @database_sync_to_async
    def set_online(self):
        self.user.status=UserStatusEnum.ONLINE
        self.user.save()

    @database_sync_to_async
    def set_offline(self):
        self.user.status = UserStatusEnum.OFFLINE
        self.user.save()
    async def disconnect(self,code):
        pass
        # self.channel_layer.group_discard(self.room_name, self.channel_name)
        # await self.set_offline()
        # print(f"user {self.user.username} disconnected  to {self.room_name} notifications")

    async def receive_json(self, content, **kwargs):
        print("received")

    async def message_received(self,event):
        message = event['message']
        print("notification received")
        # await self.send_json(message)

    async def default_handler(self,event):
        print("No handler in chat notifier")

async def notify(users):
    for user in users:
        channel_layer = get_channel_layer()
        group_name =f"user__{user.pk}"
        resp = await channel_layer.group_send(
            group_name,
            {
                'type': 'message.received',
                'message': 'dfsfsdf'
            }
        )
        print(f"user {user.username} notified  to {group_name} notifications")