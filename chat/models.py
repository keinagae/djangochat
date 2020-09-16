from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from datetime import datetime,timedelta
from django.utils import timezone
from django.utils.crypto import get_random_string
import binascii
import os

# Create your models here.
class ConversionManager(models.Manager):
    def get_room(self, user1, user2):
        print(user1.pk, user2.pk)
        conversion = self.get_queryset().filter(
            is_group=False,
            participants=user1
        ).filter(participants=user2)
        if conversion.exists():
            return conversion.first()
        else:
            conversion = Conversion.objects.create(name=get_random_string(length=12), is_group=False)
            conversion.participants.add(user1, user2)
            return conversion

    def room_exists(self,user1,user2):
        conversion = self.get_queryset().filter(
            is_group=False,
            participants=user1
        ).filter(participants=user2)
        return conversion.exists()


class WebsocketToken(models.Model):
    key = models.CharField(max_length=255,unique=True)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    expired = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        self.expired=datetime.now()+timedelta(minutes=30)
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(50)).decode()

    def is_expired(self):
        return self.expired >timezone.now()

    def __str__(self):
        return self.key

class Conversion(models.Model):
    objects = ConversionManager()
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(get_user_model())
    is_group = models.BooleanField(default=False)


class Message(models.Model):
    conversion = models.ForeignKey('chat.Conversion', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
