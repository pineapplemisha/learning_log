from django.urls import path, include

from . import views
app_name = 'users'

urlpatterns = [
    # Додати уставні url автентифікаії
    path('', include('django.contrib.auth.urls')),
    # Сторінка реєстрації
    path('register/',views.register,name='register')

]
