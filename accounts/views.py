from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def user_login(request):
    """User authorization and return of user object"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:home'))
        else:
            return HttpResponse('Error')
    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    """user logout"""
    logout(request)
    return HttpResponseRedirect(reverse('posts:home'))


def registration(request):
    """New user registration"""
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password_confirm')
        if User.objects.filter(username=username):
            return HttpResponse('A user with this username already exists')
        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Passwords do not match')
    else:
        return render(request, 'accounts/registration.html')


def personal_cabinet(request):
    return render(request, 'accounts/personal_cabinet.html')


def password_change(request):
    """Change user password"""
    if request.method == 'POST':
        user = request.user
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_password = request.POST.get('user_password')
        if user.check_password(user_password) and password1 == password2:
            user.set_password(password1)
            user.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Error')
    else:
        return render(request, 'accounts/password_change.html')
