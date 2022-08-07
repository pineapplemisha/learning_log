from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a ne user"""
    if request.method != 'POST':
        # Show empty form
        form = UserCreationForm()
    else:
        # Опраювати заповнену форму
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Авторизувати користувача і скерувати на головну сторінку
            login(request, new_user)
            return redirect('learning_logs:index')
    # Показати порожню або недійсну форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)
