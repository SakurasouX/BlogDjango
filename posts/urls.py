from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='posts'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
