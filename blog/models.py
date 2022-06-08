from django.db import models
from account.models import User


class Post(models.Model):
    title = models.CharField(max_length=300, null=False)
    date = models.DateTimeField(auto_now_add=False, null=False)
    text = models.TextField(max_length=3000, null=True)
    image = models.ImageField(upload_to='blog_images/')

    def get_summary(self):
        return self.text[:40]

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.TextField(max_length=3000, blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment[:15]