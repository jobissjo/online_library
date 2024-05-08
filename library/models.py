from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('upcoming', 'Upcoming')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False),
    author = models.CharField(max_length=50, blank=False),
    status = models.CharField(max_length=25,choices=STATUS_CHOICES, default='available')
    image_urls = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.title
    
