# coding=utf-8
import datetime
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
    phone = models.CharField('Telefonnummer', max_length=200)
    swish = models.BooleanField('har swish', default=True)

    def __str__(self):
        return str(self.name)


class Travel(models.Model):

    where = models.ForeignKey(Place)
    when = models.DateTimeField('datum för resan', default=timezone.now)
    driver = models.ForeignKey(Person)

    def __str__(self):
        return str(self.where.__str__() + " " + str(self.when.date()))

    def was_made_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.pub_date <= now

    def date(self):

        return str(self.when.date())


class Passenger(models.Model):

    trip = models.ForeignKey(Travel)
    name = models.ForeignKey(Person)

    def __str__(self):
        return str(self.name)


class MyTrip(models.Model):

    person = models.ForeignKey(Person)
    trip = models.ForeignKey(Travel)
    cost = models.IntegerField('kostnad')
    isPayed = models.BooleanField('är betald', default=False)
    payDate = models.DateTimeField('datum för betalning', default=timezone.now)

    def __str__(self):
        return str(self.person.name)








