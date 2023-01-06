from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat")
            return redirect('signup')
        else:
            messages.error(request,"Terjadi kesalahan")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
    return render(request, 'signup.html', konteks )

def index(request):
    dishes = Menu.objects.all()
    data = {
        "Title " : "Halaman Menu",
        "Heading" : "Menu Permata Catering",
        "menu" : dishes,
    }
    return render(request, "menu/index.html", data)
@login_required(login_url=settings.LOGIN_URL)
def halamanutama(request):
    dishes = Menu.objects.all()
    data = {
        "Title " : "Halaman utama",
        "Heading" : "Menu Permata Catering",
        "menu" : dishes,
    }
    return render(request, "halamanutama.html", data)
@login_required(login_url=settings.LOGIN_URL)
def halamanmenu(request):
    dishes = Menu.objects.all()
    data = {
        "Title " : "Halaman Menu",
        "Heading" : "Menu Permata Catering",
        "menu" : dishes,
    }
    return render(request, "menu/halamanmenu.html", data)

def halamanjenis(request):
    dishes = Menu.objects.all()
    data = {
        "Title " : "Halaman jenis",
        "Heading" : "Ini halaman jenis", 
        "menu" : dishes,
    }
    return render(request, "halamanjenis.html", data)
@login_required(login_url=settings.LOGIN_URL)
def halamanpeta(request):
    dishes = Menu.objects.all()
    data = {
        "Title " : "Halaman peta",
        "Heading" : "Ini halaman peta", 
        "menu" : dishes,
    }
    return render(request, "halamanpeta.html", data)

def halamandetail(request, id):
    dishes = Menu.objects.get(pk=id)
    data = {
        'Title' : "Halaman Detail menu",
        'Heading' : "Detail Menu",
        'menu' : dishes,
    }
    return render(request, "menu/halamandetail.html", data)

def createMenu(request):
    
    data = {}
    return render(request, "menu/insert.html", data)

