from django.contrib import admin
from watch.models import Mwatchlist,Swatchlist,Account,Subscribe,Freetrial
# Register your models here.
admin.site.register(Mwatchlist)
admin.site.register(Swatchlist)
admin.site.register(Account)
admin.site.register(Subscribe)
admin.site.register(Freetrial)