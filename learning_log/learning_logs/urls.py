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
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # удалить тему
    path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
    # страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # страница для редактирования записей
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # удаление записи
    path('delete_entry/<int:delete_id>/', views.delete_entry, name='delete_entry')

]
