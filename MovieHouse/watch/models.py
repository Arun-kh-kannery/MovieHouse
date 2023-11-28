from django.db import models
from movie.models import Movie
from series.models import Series
from django.contrib.auth.models import User

# Create your models here.
class Mwatchlist(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.movie

class Swatchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    def __str__(self):
        return self.series

class Freetrial(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Subscribe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.CharField(max_length=20)

class Account(models.Model):
    acctnumber=models.IntegerField()
    acctype=models.CharField(max_length=50)
    balance=models.IntegerField()

    def __str__(self):
        return str(self.acctnumber)