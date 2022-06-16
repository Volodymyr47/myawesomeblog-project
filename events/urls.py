from django.urls import path
from . import views


urlpatterns = [
    path('<int:event_id>/', views.specific_event, name='specific_event'),
    path('new_event_add/', views.new_event_add, name='new_event_add'),
    path('new_event_add/<int:event_id>/success/', views.success, name='success'),
    path('<int:event_id>/comment/', views.add_comment_to_event, name='add_comment_to_event'),
]