'''Определяем схемы urls для пользователей'''
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # включить url авторизация по умолчанию
    path('', include('django.contrib.auth.urls')),
]
