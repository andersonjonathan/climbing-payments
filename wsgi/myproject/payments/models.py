# coding=utf-8
from django.db import models
from django.utils import timezone


class Place(models.Model):
    name = models.CharField('namn', max_length=200)
    length = models.IntegerField('sträcka tur och retur i km')
    fee = models.IntegerField('kostnad att dela på')

    def __str__(self):
        return str(self.name)


class Person(models.Model):
    name = models.CharField('namn', max_length=200)

    def __str__(self):
        return str(self.name)


class Travel(models.Model):
    where = models.ForeignKey(Place)
    when = models.DateTimeField('datum för resan', default=timezone.now)
    driver = models.ForeignKey(Person)

    def __str__(self):
        return str(self.where.__str__() + " " + str(self.when) + " " + self.driver.__str__())


class Passenger(models.Model):
    trip = models.ForeignKey(Travel)
    name = models.ForeignKey(Person)

    def __str__(self):
        return str(self.name)






