from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """ Main page """
    return render(request, 'learning_logs/index.html')


def topics(request):
    """ Topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """ Show a single topic and all its entries. """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # Дані не відправленні , створити порожню форму
        form = TopicForm
    else:
        # Відправлений POST; обробити дані
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # Показати порожню або недійсну форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Жодних даних не надіслано , створити порожню форму
        form = EntryForm()
    else:
        # Отримуюі дані у POST запиті; обробити дані
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
        # Показати порожню або недійсну форму
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
