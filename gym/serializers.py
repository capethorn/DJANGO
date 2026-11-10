from rest_framework import serializers

from gym.models import (
    Additionally, Addres, AppointmentCoach, AppointmentGroup, AppointmentToGroup, Picture, 
    Subscription, Option, OptionToSubscription
)

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'price']

class OptionToSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionToSubscription
        fields = ['id', 'subscription', 'option']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'name']

class AppointmentCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentCoach
        fields = ['id', 'coach', 'user', 'data']

class AppointmentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentGroup
        fields = ['id', 'name', 'capacity', 'type', 'image']

class AdditionallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionally
        fields = ['id', 'name']

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['id', 'image']

class AddresSerializer(serializers.ModelSerializer):
    # Добавляем фиктивное поле только для чтения, чтобы отдавать готовые картинки
    album = PictureSerializer(source='pictures', many=True, read_only=True)

    class Meta:
        model = Addres
        fields = ['id', 'addres', 'image', 'pictures', 'album']

class AppointmentToGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentToGroup
        fields = ['id', 'user', 'group', 'data']

