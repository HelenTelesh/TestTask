from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.http import HttpResponse


def logout_user(request):
    return render(request, 'login/logout.html', {})


def login_form(request):
    return render(request, 'login/login.html', {})


def get_auth_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            request.user = user
            login(request, user)

            return redirect('Posts')
    return redirect('LogIn')


def index(request):
    return render(request, 'login/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User registered, {username}')
            return redirect('LogIn')
    else:
        form = UserRegisterForm()
    return render(request, 'login/signup.html', {'reg_form': form})

