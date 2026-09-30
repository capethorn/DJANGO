from rest_framework import serializers

from gym.models import Additionally, Addres, AppointmentCoach, AppointmentGroup, Subscription, Option, OptionToSubscription
from gym.models import OptionToSubscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['name', 'price']

class OptionToSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionToSubscription
        fields = ['subscription', 'option']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['name']

class AppointmentCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentCoach
        fields = ['coach', 'user', 'data']


class AppointmentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentGroup
        fields = ['name', 'capacity', 'type']

class AdditionallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionally
        fields = ['name']


class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addres
        fields = ['addres']




