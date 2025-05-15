from django.contrib import admin
from .models import Board, Comment

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority', 'state', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'board', 'text', 'date')
    readonly_fields = ('date',)