from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration', views.registration, name='registration'),
]