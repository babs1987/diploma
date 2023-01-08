from django.db import models
import datetime
from transliterate import translit




# Create your models here.

class Armwrestler(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=100, default='Бадал оглы')
    sport_category = models.CharField(max_length=4, blank=True, null=True)
    age = models.DateField(default=datetime.date(2005, 1, 1))
    sex = models.CharField(max_length=3, default='m')
    team = models.CharField(max_length=100, default="not")
    weight_category = models.CharField(max_length=4, default='60')
    #styles: ['ArmStyles']

    @property
    def en_view(self):
        fortrans = f'{self.last_name}{self.first_name}{self.id}'.lower()
        return translit(fortrans, reversed=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.CharField(max_length=99)

    students = models.ManyToManyField(Armwrestler)

    @property
    def en_view(self):
        fortrans = f'{self.last_name}{self.first_name}{self.id}'.lower()
        return translit(fortrans, reversed=True).replace("'","")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ArmStyles(models.Model):
    """
    Стили борьбы в армрестлинге
    style: имя стиля
    description: описание
    """
    style = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.style
