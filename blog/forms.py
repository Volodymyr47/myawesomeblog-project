from django.core.exceptions import ValidationError
from .models import PostComment
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment', ]


