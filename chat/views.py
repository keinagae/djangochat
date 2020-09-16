from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import WebsocketToken, Conversion, Message, get_user_model
from django.contrib.auth.models import User
from .serializers import WebSocketTokenSerializer, ConversionSerializer, MessageSerializer, UserSerializer


# Create your views here.


class ChatTokenGeneratorApiView(CreateAPIView):
    serializer_class = WebSocketTokenSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return WebsocketToken.objects.all()


class ChatListCreateApiView(ListCreateAPIView):
    serializer_class = ConversionSerializer

    def get_queryset(self):
        return Conversion.objects.filter(participants=self.request.user)


class ChatNewContactApiView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.exclude(conversion__participants=self.request.user)


class MessageListAPIView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(conversion_id=self.kwargs.get('conversion'))


def room(request, room):
    return render(request, 'room.html', {'room': room})
