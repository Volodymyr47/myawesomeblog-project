from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.


def home(request):
    events = Event.objects.filter(is_active=True)
    return render(request, 'events/home.html', {'events':events})


def specific_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/specific_event.html')