from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Event, EventsComment
from .forms import NewEvent, EventCommentForm


# Create your views here.


def home(request):
    events = Event.objects.filter(is_active=True).order_by('-updating_date')
    return render(request, 'events/home.html', {'events':events})


def specific_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # event_comment = event.eventscomment_set.order_by('-comment_date')
    event_comments = EventsComment.objects.filter(event=event_id, active=True).order_by('-comment_date')
    return render(request, 'events/specific_event.html', {'event': event, 'event_comments': event_comments})


def success(request, event_id):
    new_event = get_object_or_404(Event, pk=event_id)
    print(event_id, new_event.title)
    return render(request, 'events/success.html', {'new_event_title': new_event.title})


@login_required
def new_event_add(request):
    if request.method == 'POST':
        form = NewEvent(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            event_text = form.cleaned_data['event_text']
            event_image = form.cleaned_data['event_image']
            db_event = Event(user=request.user, title=title, event_text=event_text, event_image=event_image)
            db_event.save()
            return HttpResponseRedirect(reverse('success', args=(), kwargs={'event_id': db_event.pk}))
        else:
            return HttpResponse(status=400, content=form.errors)
    else:
        form = NewEvent()
    return render(request,'events/new_event_add.html', {'form': form})


@login_required
def add_comment_to_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except:
        return HttpResponse(status=404, content="404: Event does not exist")
    # parent_comment = EventsComment.objects.get()
    if request.method == 'POST':
        form = EventCommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            ev_comment = EventsComment(user=request.user, event=event, comment=comment)
            ev_comment.save()
            return render(request, 'events/event_comment.html')
        else:
            return HttpResponse(status=400, content=str(form.errors) + ' -> ' + str(form.is_valid()))
    else:
        return HttpResponseRedirect(reverse('home'))

