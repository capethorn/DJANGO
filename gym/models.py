

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

class AppointmentCoach(models.Model):
    coach = models.TextField("Тренер")
    user = models.TextField("Пользователь")
    data = models.DateTimeField("Дата и время")

    class Meta:
        verbose_name = "Запись к тренеру"
        verbose_name_plural = "Записи к тренеру"

    def __str__(self) -> str:
        return f"{self.user} - {self.coach}"

class AppointmentGroup(models.Model):
    name = models.TextField('Название')
    capacity = models.IntegerField('Вместимость')
    type = models.TextField('Тип')

    class Meta:
        verbose_name = "Запись на групповую тренировку"
        verbose_name_plural = "Записи на групповую тренеровку"

    def __str__(self) -> str:
        return self.name

class Additionally(models.Model):
    name = models.TextField('Название')

    class Meta:
        verbose_name = "Доп. услуга"
        verbose_name_plural = "Доп. услуги"

    def __str__(self) -> str:
        return self.name
    
class Addres(models.Model):
    addres = models.TextField('Адрес')
    
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
    
    def __str__(self) -> str:
        return self.addres