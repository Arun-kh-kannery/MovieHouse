from django.shortcuts import render,redirect
from movie.models import Movie,Genere,Language
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from series.models import Series
from watch.models import Freetrial,Subscribe
from django.contrib.auth.decorators import login_required
# Create your views here.
def base(request):
    user=request.user
    if(user.is_authenticated):
        return redirect('movie:homeall')
    return render(request,'basic.html')
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('movie:homeall')
        else:
            messages.error(request, "Invalid credentials ")
            return render(request, 'login.html')
    return render(request,'login.html')
def user_register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        e=request.POST['e']
        if(p==p1):
            try:
                u=User.objects.create_user(username=u,password=p,email=e)
                u.save()
                m=" Successfully registered now please "
                return render(request,'register.html',{'m':m})
            except:
                messages.error(request, "The username is already taken ")
                return render(request, 'register.html')
        else:
            messages.error(request, "please check your password")
            return render(request, 'register.html')
    return render(request,'register.html')
@login_required
def movie_home(request):
    m=Movie.objects.filter(trending=True)
    a=Movie.objects.filter(genere__genere__icontains="action")
    b=Movie.objects.filter(genere__genere__icontains="drama")
    c=Movie.objects.filter(genere__genere__icontains="comedy")
    d=Movie.objects.filter(genere__genere__icontains="thriller")
    return render(request,'home.html',{'m':m,'a':a,'b':b,'c':c,'d':d})
@login_required
def movie_details(request,m):
    m=Movie.objects.get(mname=m)
    return render(request,'details.html',{'m':m})
@login_required
def movie_language(request,l):
    m=Movie.objects.filter(language__language=l)
    s=Series.objects.filter(language=l)
    return render(request,'language.html',{'l':m,'s':s})
@login_required
def movie_watch(request,m):
    m=Movie.objects.get(id=m)
    user=request.user
    try:
        f = Freetrial.objects.filter(user=user)
        s = Subscribe.objects.filter(user=user)
        if (f):
            return render(request, 'movie.html', {'m': m})
        elif(s):
            return render(request, 'movie.html', {'m': m})
        else:
            return redirect('watch:subscribe')
    except:
       return redirect('watch:subscribe')



@login_required
def user_logout(request):
    logout(request)
    return redirect('movie:login')
@login_required
def home_all(request):
    m=Movie.objects.all()
    s=Series.objects.all()
    return render(request,'homeall.html',{'s':s,'m':m})
