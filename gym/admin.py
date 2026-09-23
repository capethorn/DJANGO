from django.contrib import admin

from gym.models import Option, OptionToSubscription, Subscription, AppointmentCoach, AppointmentGroup, Additionally, Addres


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(OptionToSubscription)
class OptionToSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'option')

@admin.register(AppointmentCoach)
class AppointmentCoachAdmin(admin.ModelAdmin):
    list_display = ('coach', 'user', 'data')

@admin.register(AppointmentGroup)
class AppointmentGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'type')

@admin.register(Additionally)
class AdditionallyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Addres)
class AddresAdmin(admin.ModelAdmin):
    list_display = ('addres',)