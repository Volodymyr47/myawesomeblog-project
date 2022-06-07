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


def comentadd(request):
    return render(request, 'blog/comment.html')


def success(request):
    return render(request, 'blog/success.html')


def add_comment_to_post(request, post_id):
    # if post_id and user_id:
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            # form.save(commit=False)
            post = post_id
            user = request.user.id
            form.save()
            # comentadd(request, post_id)
            # return HttpResponseRedirect('comentadd')
            return render(request, 'blog/success.html')
            # return super().form_valid(form)
        else:
            return HttpResponse(status=400, content=str(form.errors))
    else:
        return HttpResponseRedirect(reverse('showblog'))
    # else:
    #     return HttpResponse(status=400, content=str(user_id)+' '+str(post_id))



