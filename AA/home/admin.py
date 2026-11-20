from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'user', 'created_at', 'is_published']
    list_filter = ['user', 'is_published']
    search_fields = ['title', 'body']
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    list_editable = ('is_published',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','created_at','is_reply']
    list_filter = ['user','is_reply']
    search_fields = ['user','body']
    ordering = ('-created_at',)
    raw_id_fields = ('user',)