from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, **NULLABLE, related_name='milage_car',
                            verbose_name='машина')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, **NULLABLE, related_name='milage_moto',
                             verbose_name='мотоцикл')

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.SmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробег'
        ordering = ('-year',)
