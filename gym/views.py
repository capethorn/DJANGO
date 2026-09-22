from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from gym.models import Subscription
from django.views.generic import TemplateView
from gym.models import OptionToSubscription

# Create your views here.
# class ShowSubscriptionView(TemplateView):
#     template_name = "gym/show_subscription.html"

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['gym'] = Subscription.objects.all()

#         return context


class ShowSubscriptionView(TemplateView):
    template_name = "gym/show_subscription.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['gym'] = OptionToSubscription.objects.all()

        return context