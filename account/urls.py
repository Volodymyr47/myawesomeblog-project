from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('registration/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name = 'login'),
]

