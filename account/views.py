from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.


def register(request):
    '''
    User registrations function
    '''
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
