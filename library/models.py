from django.db import models
import uuid
from django.contrib.auth.models import User


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=50, blank=False)
    genre = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=25, default='available')
    image_url = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')

    borrowed_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
