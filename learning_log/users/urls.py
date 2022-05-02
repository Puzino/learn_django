'''Определяем схемы urls для пользователей'''
from django.urls import include, path

from . import views

app_name = 'users'
urlpatterns = [
    # включить url авторизация по умолчанию
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
