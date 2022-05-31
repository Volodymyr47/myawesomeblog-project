from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('registration/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout_view')
]

