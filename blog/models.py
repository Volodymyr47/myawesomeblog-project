from django.db import models
from account.models import User


# Create your models here.

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
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    class Meta:
        ordering = ('comment_date',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)