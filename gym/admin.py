from django.contrib import admin

from gym.models import Option, OptionToSubscription, Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(OptionToSubscription)
class OptionToSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'option')