from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('registration/', views.registration, name='registration'),
    path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('password_change/', views.password_change, name='password_change'),
    path('logout/', views.user_logout, name='user_logout'),
]
