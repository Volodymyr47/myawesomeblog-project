from django.shortcuts import render, get_object_or_404
from .models import Post, PostComment
from .forms import CommentForm
from django.contrib.auth.models import User




# Create your views here.

def showblog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})


def specific_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = PostComment.objects.filter(post=post_id).order_by('-comment_date')
    return render(request,'blog/specific_post.html', {'post': post, 'comments': comments})


def add_comment_to_post(request):
    post_id = Post.id
    user_id = User.id
    if request.method == 'POST':
        try:
            # comment_post = CommentForm(data=request.POST)
            comment_post = PostComment(post=post_id, user=user_id,comment=CommentForm.fields.comment, active=False)
            if comment_post.is_valid():
                comment_post.save()
        except Exception as e:
            raise(f'Error exception with insert data to PostComment: {e.__str__()}')
            print(f'Error exception with insert data to PostComment: {e.__str__()}')
    else:
        return CommentForm()
