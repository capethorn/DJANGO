from django.db import models

class Subscription(models.Model):
    name = models.TextField("Название")
    price = models.IntegerField("Цена")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self) -> str:
        return self.name
    
class Option(models.Model):
    name = models.TextField("Название")

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"

    def __str__(self) -> str:
        return self.name

class OptionToSubscription(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Опция к подписке"
        verbose_name_plural = "Опции к подпискам"

    def __str__(self) -> str:
        return f"{self.subscription} - {self.option}"