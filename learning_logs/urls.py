""" Urls pattern for learning_logS"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
    # Сторінка , що відображає всі теми
    path('topics/', views.topics, name='topics'),
    # Сторінка , що присвячена кожній темі
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Сторінка для додавання нової теми
    path('new_topic/',views.new_topic,name='new_topic'),
    # Сторінка для додавання нових статтей
    path("new_entry/<int:topic_id>/",views.new_entry,name='new_entry'),

]
