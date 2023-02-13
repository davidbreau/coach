from django.shortcuts import render, redirect
from django.conf import settings
from .forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'app/index.html')


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
        request, 'app/authentication/log_in.html', context={'form': form, 'message': message})
    
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
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'app/authentication/sign_up.html', context={'form': form})

@login_required
def rdv(request):
    return render(request, 'app/rdv.html')

