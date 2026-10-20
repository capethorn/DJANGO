from rest_framework import serializers

from gym.models import (
    Additionally, Addres, AppointmentCoach, AppointmentGroup, 
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
        fields = ['id', 'name', 'capacity', 'type']

class AdditionallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionally
        fields = ['id', 'name']

class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addres
        fields = ['id', 'addres']



