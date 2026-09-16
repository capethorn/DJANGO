from django.db import models

class Subscription(models.Model):
    name = models.TextField("Название")
    price = models.IntegerField("Цена")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

# class Option(models.Model):знер
#     name = models.TextField("Название")
    
# class OptionToSubscription(models.Model):
#     subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
#     option = models.ForeignKey(Option, on_delete=models.CASCADE)