from django.db import models


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