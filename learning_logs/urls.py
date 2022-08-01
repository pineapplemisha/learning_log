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

]
