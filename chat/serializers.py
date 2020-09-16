from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Conversion, Message, WebsocketToken


class WebSocketTokenSerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)

    class Meta:
        model = WebsocketToken
        fields = [
            'key',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.update(user=user)
        WebsocketToken.objects.filter(user=user).delete()
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username'
        ]


class ConversionSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True,read_only=True)
    name=serializers.CharField(required=False)
    participants_id = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all()), write_only=True,
        source='participants')
    user = serializers.SerializerMethodField()

    def get_user(self, obj: Conversion):
        if obj.is_group:
            return {}
        else:
            return UserSerializer(obj.participants.exclude(id=self.context['request'].user.id).first()).data

    class Meta:
        model = Conversion
        fields = [
            'name',
            'id',
            'is_group',
            'participants',
            'user',
            'participants_id'
        ]

    def validate(self,attrs):
        participants=attrs['participants']
        if Conversion.objects.room_exists(participants[0],self.context['request'].user):
            raise serializers.ValidationError("Room exists")
        attrs['participants'].append(self.context['request'].user)
        return attrs


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Message
        fields = [
            'message',
            'conversion',
            'id',
            'user'
        ]
