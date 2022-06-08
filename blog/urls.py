from django.urls import path
from . import views

urlpatterns = [
    path('', views.showblog, name='showblog'),
    path('<int:post_id>/', views.specific_post, name='specific_post'),
    path('<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('<int:post_id>/comment/', views.commentadd, name='commentadd'),
]
