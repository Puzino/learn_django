from django.urls import path
from . import views

app_name = 'meal_plans_logs'
urlpatterns = [
    path('', views.index, name='index'),
]
