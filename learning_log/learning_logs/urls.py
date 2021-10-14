"""Определяет схемы url для learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # домашняя страница
    path('', views.index, name='index'),
    # страница со списком тем
    path('topics/', views.topics, name='topics'),
    # страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
