from django.shortcuts import redirect, render
from django.http import HttpResponse
from app1.models import contactm
from app1.models import contactm2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")
def page1(request):
    return render(request,"page1.html")
def Premchand(request):
    return render(request,"Premchand.html")
def Tagore(request):
    return render(request,"Tagore.html")
def Arundhati(request):
    return render(request,"Arundhati.html")
def biography(request):
    return render(request,"biography.html")
def home(request):
    return render(request,"home.html")
def login1(request):
    return render(request,"login.html")
def loginform(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    User=authenticate(username=username,password=password)

    if User is not None:
        login(request,User)
        return redirect('/home')
    else:
        return redirect('/login')

def contactM(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        r=contactm(username=username,email=email)
        r.save()
        r1=contactm2(username=username,email=email)
        r1.save()
        return render(request,"index.html",{'msg':'We Will Try To Contact You Soon'})

def change(request):
    return render(request,"change.html")
def changepassword(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        r=User.objects.get(username=username)
        r.set_password(password)
        r.save()
        return render(request,"change.html",{'msg':'Successfully Changed Password'})
        #return HttpResponse(username)

def all(request):
    r=contactm.objects.all
    return render(request,"all.html",{'data':r})


def delete(request):
    return render(request,"delete.html")
def erase(request):
    if request.method=="POST":
        username=request.POST.get('username')
        r=contactm.objects.filter(username=username)
        r.delete()
        return render(request,"delete.html",{'msg':'Succesfully Deleted'})


def update(request):
    return render(request,"update.html")
def userupdate(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        contactm.objects.filter(username=username,email=email)
        return render(request,"update.html",{'msg':'Successfully Updated'})


def search(request):
    return render(request,"search.html")
def usersearch(request):
    if request.method=="POST":
        username=request.POST.get('username')
        r=contactm.objects.get(username=username)
        return render(request,"search.html",{'data':r})


def userlogout(request):
    logout (request)
    return redirect('/index')


def permanent(request):
    #return render(request,'permanent.html')
    r1=contactm2.objects.filter
    return render(request,"permanent.html",{'data':r1})