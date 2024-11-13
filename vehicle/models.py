from config import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    amount = models.IntegerField(default=1000, verbose_name='сумма')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='цена')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, related_name='car_owner',
                              verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='цена')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, related_name='moto_owner',
                              verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, **NULLABLE, related_name='milage',
                            verbose_name='машина')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, **NULLABLE, related_name='milage',
                             verbose_name='мотоцикл')

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.SmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробег'
        ordering = ('-year',)
