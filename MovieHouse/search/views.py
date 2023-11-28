from django.shortcuts import render
from movie.models import Movie
from series.models import Series
# Create your views here.
def searchresult(request):
    query=""
    if(request.method=="POST"):
        query=request.POST['q']
        try:
            if(query):
              m=Movie.objects.filter(mname__icontains=query)
              s=Series.objects.filter(sname__icontains=query)
            return render(request,'result.html',{'m':m,'s':s,'q':query})
        except:
            return render(request,'result.html',{'q':query})