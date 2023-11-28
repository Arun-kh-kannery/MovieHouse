from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Genere(models.Model):
    genere=models.CharField(max_length=100)
    def __str__(self):
        return self.genere
class Language(models.Model):
    language=models.CharField(max_length=100)

    def __str__(self):
        return self.language

class Movie(models.Model):
    mname=models.CharField(max_length=100)
    image=models.ImageField(upload_to="movie/movies",blank=True,null=True)
    year=models.CharField(max_length=50)
    duration=models.CharField(max_length=100)
    rating_outof_10=models.IntegerField()
    cover=models.ImageField(upload_to="movies/cover",blank=True,null=True)
    description=models.TextField()
    genere=models.ForeignKey(Genere,on_delete=models.CASCADE)
    trending=models.BooleanField(default=False)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)
    video=models.FileField(upload_to="movies/videos",max_length=500)
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.mname