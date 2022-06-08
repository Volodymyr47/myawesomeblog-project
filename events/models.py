from django.db import models
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()


# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updating_date = models.DateTimeField(auto_now=True)
    event_text = models.TextField(blank=False)
    event_image = models.ImageField(upload_to='', blank=False)
    is_active = models.BooleanField(default=False)

    def get_title(self):
        return self.title[:40]

    def __str__(self):
        return self.title[:20]

