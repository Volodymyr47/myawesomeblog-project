from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(User):
    user_name = models.CharField(max_length=100, blank=False, unique=True)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    user_email = models.EmailField(max_length=200, blank=False, unique=True, help_text='eg. volodymyr.di@gmail.com')
    passwd = models.CharField(max_length=100, blank=False)


def user_creation(request, user_name, user_email, passwd, firstname, lastname):
    new_user = User.objects.create_user(user_name, user_email, passwd, firstname, lastname)
    new_user.save()

