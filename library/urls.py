
from django.urls import path
from .views import BookCreateView,BookRetrieveUpdateDeleteView, BookListView, BookCreateListView


urlpatterns = [
    path('', BookCreateListView.as_view(), name='book-create'),
    path('<uuid:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail')
]