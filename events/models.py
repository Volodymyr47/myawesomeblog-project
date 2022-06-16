from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updating_date = models.DateTimeField(auto_now=True)
    event_text = models.TextField(blank=False)
    event_image = models.ImageField(upload_to='ev_images/', blank=False)
    is_active = models.BooleanField(default=False)

    def get_title(self):
        return self.title[:40]

    def __str__(self):
        return self.title[:20]


class EventsComment(models.Model):
    event = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', null=True, on_delete=models.SET_NULL)
    # parent_id = models.IntegerField(default=-1)
    comment = models.TextField(blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment[:15]

    # def _parent_id(self, )

# class EventsCommentReply(models.Model):
#     comment = models.ForeignKey(EventsComment, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#     rep_comment = models.TextField(blank=False)
#     rep_date = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.rep_comment[:15]
