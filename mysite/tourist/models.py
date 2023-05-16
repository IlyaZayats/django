from django.db import models
from django.urls import reverse

class Clients(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    passport = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.name, self.last_name, self.middle_name)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def get_name(self):
        return "tourist"

class Seasons(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    start = models.DateField()
    end = models.DateField()
    closed = models.IntegerField(max_length=1)

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.start, self.end, self.closed)

    def get_absolute_url(self):
        return reverse('seasons-detail', args=[str(self.id)])

    def get_name(self):
        return "seasons"

class Tours(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    season_id = models.ForeignKey('Seasons', on_delete=models.CASCADE)
    price = models.IntegerField(max_length=20)
    city = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    info = models.CharField(max_length=120)

    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.season_id, self.name, self.info, self.price)

    def get_absolute_url(self):
        return reverse('tours-detail', args=[str(self.id)])

    def get_name(self):
        return "tours"

class Trips(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    tour_id = models.ForeignKey('Seasons', on_delete=models.CASCADE)
    client_id = models.ForeignKey('Clients', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.id, self.tour_id, self.client_id)

    def get_absolute_url(self):
        return reverse('trips-detail', args=[str(self.id)])

    def get_name(self):
        return "trips"


