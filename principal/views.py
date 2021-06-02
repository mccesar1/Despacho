from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .models import Reportes, Declaraciones




def inicio(request):
    return render(request, 'index.html')


def contacto(request):
    if request.method == "POST":
        asunto = request.POST["name"]
        mensaje = request.POST["message"] + " / Email: " + request.POST["email"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["cesarlazarus123@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoexitoso.html")
    return render(request, "contacto.html")


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/welcome')

    return render(request, "login.html", {'form': form},)


@login_required
def welcome(request):
    id = request.user.id
    data = Reportes.objects.get(id=id)
    datos = Reportes.objects.filter(nombre=id)

    return render(request, "welcome.html",  {

            'datos': datos,
            'data': data,
        })


@login_required
def reportes(request):
    id = request.user.id
    datos = Reportes.objects.filter(nombre=id)

    return render(request,"reportes.html", {
        'datos': datos,

    })


@login_required
def declaraciones(request):
        id = request.user.id
        datos = Declaraciones.objects.filter(nombre=id)

        return render(request, "declaraciones.html", {
            'datos': datos,

        })


def logout(request):
    do_logout(request)
    return redirect('/')
