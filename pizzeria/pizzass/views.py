from django.shortcuts import render
from .models import Topping


def index(request):
    return render(request, 'pizzass/index.html')

def topics(request):
    """Выводит список тем"""
    topics = Topping.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'pizzass/topics.html', context)

def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topping.objects.get(id=topic_id)

    context = {'topic': topic}
    return render(request, 'pizzass/topic.html', context)