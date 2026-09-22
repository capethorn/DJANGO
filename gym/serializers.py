from rest_framework import serializers

from gym.models import Subscription
from gym.models import OptionToSubscription

# class SubscriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscription
#         fields = ['name', 'price']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionToSubscription
        fields = ['subscription', 'option']