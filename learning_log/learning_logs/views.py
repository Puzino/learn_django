from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    # домашняя страница
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    # проверка того, что темa принадлежит текущему пользователю
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST' :
        # данные не отправлялись: создается пустая форма
        form = TopicForm()
    else:
        # отправленные данные 'POST': обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # выведет пустую или недействительную форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # данные не отправлялись: создается пустая форма
        form = EntryForm()
    else:
        # отправленные данные 'POST': обработать данные
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # выведет пустую или недействительную форму
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Редактирование существущующей записи"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # проверка того, что тему принадлежит текущему пользователю
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # исходный запрос: форма заполняется данными текущей
        form = EntryForm(instance=entry)
    else:
        # отправленные данные 'POST': обработать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

# def delete_entry(request, entry_id):
    
# # def delete_new(request, new_id):
#     new_to_delete = get_object_or_404(Entry, id=entry_id)
#     #+some code to check if this object belongs to the logged in user

#     if request.method == 'POST':
#         form = DeleteNewForm(request.POST, instance=new_to_delete)

#         if form.is_valid(): # checks CSRF
#             new_to_delete.delete()
#             return HttpResponseRedirect("/") # wherever to go after deleting

#     else:
#         form = DeleteNewForm(instance=new_to_delete)

#     context = {'form': form}
#     return render(request, 'learning_logs/delete_entry.html', context)