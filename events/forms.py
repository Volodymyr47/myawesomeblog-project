from .models import Event, EventsComment
from django import forms


class NewEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_text', 'event_image']


class EventCommentForm(forms.ModelForm):
    class Meta:
        model = EventsComment
        fields = ['comment',]

