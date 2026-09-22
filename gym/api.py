from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from gym.models import Subscription
from gym.serializers import SubscriptionSerializer
from gym.models import OptionToSubscription

class SubscriptionViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = OptionToSubscription.objects.all()
    serializer_class = SubscriptionSerializer