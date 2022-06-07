from django.contrib import admin
from .models import Post #PostComment
from .models import User
from .forms import PostComment


# Register your models here.

admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    def __username(self):
        user_name = User.objects.filter(User.id)

    def __posttitle(self):
        posttitle = Post.objects.filter(p_id=Post.id)

    list_display = ('comment_date', 'comment', 'active')
    list_filter = ('comment_date', )
    search_fields = ('comment',)


admin.site.register(PostComment, CommentAdmin)