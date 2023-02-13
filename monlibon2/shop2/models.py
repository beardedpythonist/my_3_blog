from django.db import models


class Parts(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    brand = models.CharField(max_length=50, verbose_name='Производитель')
    artikul = models.TextField(null=True, blank=True, verbose_name='Номер')
    price = models.FloatField(null=True, blank=True, verbose_name='цена' )
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT)
    car_name = models.ForeignKey('Car_name', null=True, on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Запчасти'
        verbose_name = 'Запчасть'


class Rubric(models.Model):
    name = models. CharField(max_length=20, db_index=True,
                             verbose_name='Категория')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']


class Car_name(models.Model):
    name = models. CharField(max_length=20, db_index=True,
                             verbose_name='Марка авто')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Марки'
        verbose_name = 'Марка'
        ordering = ['name']