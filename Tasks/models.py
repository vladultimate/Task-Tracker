from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATE_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=15,
        choices=PRIORITY_CHOICES,
        default='medium',
    )
    state = models.CharField(
        max_length=30,
        choices=STATE_CHOICES,
        default='not_started',
    )
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    disliked_by = models.ManyToManyField(User, related_name='disliked_comments', blank=True)

    def like_count(self):
        return self.liked_by.count()

    def dislike_count(self):
        return self.disliked_by.count()