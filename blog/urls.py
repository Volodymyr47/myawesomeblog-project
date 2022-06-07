from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showblog, name='showblog'),
    path('<int:post_id>/', views.specific_post, name='specific_post'),
    path('<int:post_id>/success/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<int:post_id>/comment/', views.comentadd, name='comentadd'),
]
