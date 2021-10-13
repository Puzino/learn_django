from django.urls import path
from . import views

app_name = 'pizzass'
urlpatterns = [
    path('', views.index, name='index')
]
