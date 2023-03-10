from django.shortcuts import render, redirect
from django.conf import settings
from .models import Appointment
from core.forms import LoginForm, SignupForm, AppointForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.contrib import messages
from django.views.generic.edit import CreateView

@login_required
def index(request):
    return render(request, 'core/index.html')


def log_in(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('index')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'core/authentication/log_in.html', context={'form': form, 'message': message})
    
def logout_user(request):
    
    logout(request)
    return redirect('log_in')


def sign_up(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('index')
    return render(request, 'core/authentication/sign_up.html', context={'form': form})

@login_required
def rdv(request):
    form = AppointForm
    if request.method == 'POST':
        form = AppointForm(request.POST)
        user = request.user
        if form.is_valid():
            cd = form.cleaned_data
            rendez_vous = Appointment(
                user = request.user,
                name = cd['name'],
                date = cd['date'],
                time = cd['time'],
                message = cd['message']
            )
            rendez_vous.save()
    else:
        form = AppointForm()
    return render(request, 'core/rdv.html', context={'form': form})

def about(request):
    return render(request, 'core/about.html')

@login_required
def seerdv(request):
    appointments = Appointment.objects.all()
    if request.user.is_staff:
        return render(request, 'core/seerdv.html', {'appointments': appointments})
    else:
        return render(request, 'index')