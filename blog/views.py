import this

from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from .forms import PostComment
# from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def showblog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})


def specific_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = PostComment.objects.filter(post=post_id).order_by('-comment_date')
    return render(request, 'blog/specific_post.html', {'post': post, 'comments': comments})



def add_comment_to_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponse(status=404, content="404: Post does not exist")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(request.user.id, post_id)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            # form.save(commit=False)
            # post = post_id
            # user = request.user.id
            db_comment = PostComment(user=request.user, post=post, comment=comment)
            db_comment.save()
            # form.save()
            return render(request, 'blog/comment.html')
        else:
            return HttpResponse(status=400, content=str(form.errors) + ' -> ' + str(form.is_valid()))
    else:
        return HttpResponseRedirect(reverse('showblog'))




