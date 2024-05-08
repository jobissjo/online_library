from django.urls import path
from .views import BookCreateView,BookRetrieveUpdateDeleteView


urlpatterns = [
    path('', BookCreateView.as_view(), name='book_create'),
    path('<uuid:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book_get_update_delete')
]