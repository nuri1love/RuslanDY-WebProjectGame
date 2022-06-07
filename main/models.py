from django.db import models
from simple_history.models import HistoricalRecords


class Enemy(models.Model):
    
    enemy_name = models.CharField(verbose_name='Имя противника' , max_length=40)
    story = models.TextField(verbose_name='Бестиарий')
    hpoints = models.FloatField(verbose_name='Жизни')
    lvl = models.FloatField(verbose_name='Уровень противника')
    type = models.CharField(verbose_name='Тип противника', max_length=40)

    history = HistoricalRecords()

    def __str__(self):
        return self.enemy_name

    class Meta:
        verbose_name = 'Противник'
        verbose_name_plural = 'Противники'


class Skill(models.Model):
    title = models.CharField(verbose_name='Название способности', max_length=255)
    category = models.CharField(verbose_name='Категория' , max_length=255)
    cost = models.FloatField(verbose_name='Цена прокачки')

    def __str__(self):
        return self.title
    
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

class Thing(models.Model):
    title = models.CharField(verbose_name='Название предмета', max_length=255)
    damage = models.FloatField(verbose_name='Урон')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.title
    
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Location(models.Model):
    name_loc = models.CharField(verbose_name='Название локации', max_length=255)
    histoty = models.TextField(verbose_name='История локации')
    enemy = models.ManyToManyField(Enemy, verbose_name='Противник')
    thing = models.ManyToManyField(Thing, verbose_name='Предмет после прохождения')

    history = HistoricalRecords()

    def __str__(self):
        return self.name_loc


    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
