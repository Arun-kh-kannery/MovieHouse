from django.db import models

# Create your models here.

class Series(models.Model):
    sname=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="series/image",null=True,blank=True)
    video=models.FileField(upload_to="series/videos")
    language=models.CharField(max_length=100)
    rating_outof_10=models.IntegerField()
    season=models.IntegerField()
    no_of_episodes=models.IntegerField(default=5)

    def __str__(self):
        return self.sname
