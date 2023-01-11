from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    display_posts = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'post')
    list_filter = ('created_at',)
    search_fields = ('author', 'content')
    actions = ['approve comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)