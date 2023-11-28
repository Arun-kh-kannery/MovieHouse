from django.contrib import admin
from movie.models import Genere,Language,Movie
# Register your models here.
admin.site.register(Genere)
admin.site.register(Language)
admin.site.register(Movie)

