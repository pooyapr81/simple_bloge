from django.contrib import admin
from .models import Post, Comment, Vote


class PostAdmin(admin.ModelAdmin):
    list_display = ('use', 'slug', 'updated')
    search_fields = ('slug', 'body')
    list_filter = ('created', 'updated')
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('use',)


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')


admin.site.register(Vote)
