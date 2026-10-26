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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from gym import views
from rest_framework.routers import DefaultRouter

from gym.api import AdditionallyViewset, AddresViewset, AppointmentCoachViewset, AppointmentGroupViewset, AppointmentToGroupViewset, OptionToSubscriptionViewset, OptionViewset, SubscriptionViewset

router = DefaultRouter()
router.register("subscription", SubscriptionViewset, basename="subscription")
router.register("option", OptionViewset, basename="option")
router.register("option-to-subscription", OptionToSubscriptionViewset, basename="option-to-subscription")
router.register("appointment-coach", AppointmentCoachViewset, basename="appointment-coach")
router.register("appointment-group", AppointmentGroupViewset, basename="appointment-group")
router.register("additionally", AdditionallyViewset, basename="additionally")
router.register("addres", AddresViewset, basename="addres")
router.register("appointment-to-group", AppointmentToGroupViewset, basename="appointment-to-group")

urlpatterns = [
    path('', views.ShowSubscriptionView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
