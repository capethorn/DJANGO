from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from gym.models import Subscription, Option, OptionToSubscription, AppointmentCoach, AppointmentGroup, Additionally
from gym.serializers import SubscriptionSerializer, OptionSerializer, OptionToSubscriptionSerializer, AppointmentCoachSerializer, AppointmentGroupSerializer, AdditionallySerializer


class SubscriptionViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class OptionViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class OptionToSubscriptionViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = OptionToSubscription.objects.all()
    serializer_class = OptionToSubscriptionSerializer

class AppointmentCoachViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = AppointmentCoach.objects.all()
    serializer_class = AppointmentCoachSerializer

class AppointmentGroupViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = AppointmentGroup.objects.all()
    serializer_class = AppointmentGroupSerializer

class AdditionallyViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Additionally.objects.all()
    serializer_class = AdditionallySerializer