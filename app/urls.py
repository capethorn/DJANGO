"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from gym import views

from rest_framework.routers import DefaultRouter

from gym.api import SubscriptionViewset

router = DefaultRouter()
router.register("gym", SubscriptionViewset, basename="gym")
router.register("subscription", SubscriptionViewset, basename="subscription")
router.register("option", SubscriptionViewset, basename="option")
router.register("option-to-subscription", SubscriptionViewset, basename="option-to-subscription")
router.register("appointment-coach", SubscriptionViewset, basename="appointment-coach")
router.register("appointment-group", SubscriptionViewset, basename="appointment-group")
router.register("additionally", SubscriptionViewset, basename="additionally")
router.register("addres", SubscriptionViewset, basename="addres")

urlpatterns = [
    path('', views.ShowSubscriptionView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
