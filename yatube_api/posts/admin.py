from django.contrib import admin

from .models import Comment, Follow, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'created',
    )


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'following',
        'id'
    )


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
