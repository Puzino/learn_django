from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Регестрируем нового пользователя"""
    if request.method != 'POST':
        # Выводит пустую форму
        form = UserCreationForm()
    else:
        # обработка заполненной формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)
