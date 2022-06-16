# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
#
# class SignUpForms(UserCreationForm):
#     first_name = forms.CharField(max_length=100, required=False)
#     last_name = forms.CharField(max_length=100, required=False)
#     user_name = forms.CharField(max_length=50, required=True)
#     email = forms.EmailField(max_length=250, help_text='eg. volodymyr.di@gmail.com')
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'password1', 'password2')