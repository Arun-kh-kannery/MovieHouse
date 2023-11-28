from django.shortcuts import render,redirect
from movie.models import Movie
from series.models import Series
from movie.models import Movie
from django.contrib import messages
from watch.models import Mwatchlist,Swatchlist,Freetrial,Subscribe,Account
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_to_watchlist(request,pk):
    m=Movie.objects.get(pk=pk)
    user=request.user
    try:
        w=Mwatchlist.objects.filter(user=user,movie=m)
        w.delete()
        w = Mwatchlist.objects.create(movie=m, user=user)
        w.save()
    except:
        w=Mwatchlist.objects.create(movie=m,user=user)
        w.save()
    return redirect('watch:Mwatchlist')
@login_required
def viewwatchlist(request):
    user = request.user
    s = Swatchlist.objects.filter(user=user)
    return render(request, 'watchlist.html', {'s':s})
@login_required
def viewMwatchlist(request):
    user=request.user
    m= Mwatchlist.objects.filter(user=user)
    return render(request,'Mwatchlist.html', {'m': m})
@login_required
def add_to_Swatchlist(request,pk):
    m = Series.objects.get(pk=pk)
    user = request.user
    try:
        w = Swatchlist.objects.get(user=user, series=m)
        w.delete()
        w = Swatchlist.objects.create(series=m, user=user)
        w.save()
    except:
        w = Swatchlist.objects.create(series=m, user=user)
        w.save()
    return redirect('watch:watchlist_view')
@login_required
def mremove(request,pk):
    m=Mwatchlist.objects.get(pk=pk)
    m.delete()
    return viewMwatchlist(request)
@login_required
def sremove(request,pk):
    s=Swatchlist.objects.get(pk=pk)
    s.delete()
    return viewwatchlist(request)
def subscribe(request):
    user=request.user
    try:
        f = Freetrial.objects.get(user=user)
        return render(request,'subscribe.html',{'f':f})
    except:
        return render(request,'subscribe.html')

def freetrial(request):
    user=request.user
    f = Freetrial.objects.create(user=user)
    f.save()
    return redirect('movie:homeall')
def subscription(request):
    if(request.method=="POST"):
        n=request.POST['n']
        user=request.user
        amount=49
        try:
            acct = Account.objects.get(acctnumber=n)
            if (acct.balance >= amount):
                acct.balance -= amount
                acct.save()
                s = Subscribe.objects.create(user=user, amount=amount)
                s.save()
                msg = "subscribed successfully"
                return render(request, 'subscribeconfirm.html', {'msg': msg})
            else:
                msg = "Insufficient Balance.You Cant Place Order"
                return render(request, 'subscribeconfirm.html', {'msg': msg})
        except:
            messages.error(request, "Invalid accountnumber ")
            return render(request,'subscription.html')
    return render(request,'subscription.html')
def subscription2(request):
    if (request.method == "POST"):
        n = request.POST['n']
        user = request.user
        amount = 500
        try:
            acct = Account.objects.get(acctnumber=n)
            if (acct.balance >= amount):
                acct.balance -= amount
                acct.save()
                s = Subscribe.objects.create(user=user, amount=amount)
                s.save()
                msg = "subscribed successfully"
                return render(request, 'subscribeconfirm.html', {'msg': msg})
            else:
                msg = "Insufficient Balance.You Cant Subscribe"
                return render(request, 'subscribeconfirm.html', {'msg': msg})
        except:
            messages.error(request, "Invalid accountnumber ")
            return render(request, 'subscription2.html')
    return render(request,'subscription2.html')

