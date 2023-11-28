from django.shortcuts import render,redirect
from series.models import Series
from watch.models import Freetrial,Subscribe
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def series_home(request):
    s=Series.objects.all()
    return render(request,'shome.html',{'s':s})
@login_required
def series_details(request,pk):
    s=Series.objects.get(pk=pk)
    l=s.no_of_episodes
    return render(request,'sdetails.html',{'s':s,'range':range(1,l+1)})
@login_required
def series_view(request,pk):
    user=request.user
    try:
        f= Freetrial.objects.get(user=user)
        if (f):
            s = Series.objects.get(pk=pk)
            return render(request, 'series.html', {'s': s})
        else:
            return redirect('watch:subscribe')
    except:
        s = Subscribe.objects.filter(user=user)
        if (s):
            s = Series.objects.get(pk=pk)
            return render(request, 'series.html', {'s': s})
        return redirect('watch:subscribe')
@login_required
def series_episodes(request,pk):
    s = Series.objects.get(pk=pk)
    l = s.no_of_episodes
    return render(request, 'episodes.html', {'s': s, 'range': range(1, l + 1)})
