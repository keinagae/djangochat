from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserStatusEnum(models.TextChoices):
    ONLINE='online',
    OFFLINE='offline'

class User(AbstractUser):
    status=models.CharField(choices=UserStatusEnum.choices,max_length=50,default=UserStatusEnum.OFFLINE)
