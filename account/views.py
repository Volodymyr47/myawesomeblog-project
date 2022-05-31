from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.


def register(request):
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
    return HttpResponseRedirect(reverse('showblog'))


# def login(request):
#     return render(request, 'registration/login.html')
#
#
# def registration(request):
#     return render(request, 'account/registration.html')
#
#
# def welcome(request):
#     return render(request, 'account/welcome.html')
#
#
# def logout(request):
#     return render(request, 'registration/logout.html')
#
#
# def password_reset(request):
#     return render(request, 'account/password_reset.html')
#
#
# def password_reset_done(request):
#     return render(request, 'account/password_reset_done.html')