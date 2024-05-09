from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField( source='pk', read_only=True)
    created_at = serializers.DateTimeField( read_only=True)
    
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'status', 'genre' ,'image_url','description', 'created_at']