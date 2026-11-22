'''
Currently no models at this point in development due to us using the default django
AUTH_USER_MODEL

Will add the Notes model soon...
'''

from django.db  import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    content = models.TextField(max_length=300, verbose_name="Task")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
