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

class BorrowRequest(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    REQUEST_STATUS = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected')
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=REQUEST_STATUS, default=PENDING)

    def approve_request(self):
        if self.status == 'pending':
            self.status = 'approved'
            self.book.status = 'not available'
            self.book.borrowed_user = self.borrower
            self.book.save()
            self.save()