from django.db import models
from datetime import datetime

class Specialist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Тип')
    rate = models.FloatField(default=1, verbose_name='Ставка')
    def save(self, *args, **kwargs):
        log = ChangeLog.objects.all()[0]
        log.value += 1
        log.date = datetime.now()
        log.save()
        super(Specialist, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
URIST_ID = 1
class Works(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=500, verbose_name='Название')
    specialist_type = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='specialist_type', default=URIST_ID, verbose_name="Тип специалиста")
    hours = models.DecimalField(max_digits=5, decimal_places=2, default=1, null=True, blank=True, verbose_name="Часы")
    count = models.IntegerField(default=1, null=True, blank=True, verbose_name="Количество")
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        log = ChangeLog.objects.all()[0]
        log.value += 1
        log.date = datetime.now()
        log.save()
        super(Works, self).save(*args, **kwargs)
    class Meta:
        ordering = ['number']
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500, verbose_name="Название")
    services = models.ManyToManyField(Works, related_name='services', verbose_name="Услуги")
    isOriginal = models.BooleanField(default=True, verbose_name="Оригинальная работа")
    def save(self, *args, **kwargs):
        log = ChangeLog.objects.all()[0]
        log.value += 1
        log.date = datetime.now()
        log.save()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class ChangeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.IntegerField(default=1)
    date = models.DateTimeField(null=True, blank=True)



# Create your models here.
