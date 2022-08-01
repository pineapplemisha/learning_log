from django.db import models


class Topic(models.Model):
    """Тема ,яку вивчає користувач"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Повернути рядкове представлення моделі"""
        return self.text


class Entry(models.Model):
    """Конкретна інформація з цієї теми"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text