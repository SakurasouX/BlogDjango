from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('text_render', views.form_text, name='text_render'),
]
