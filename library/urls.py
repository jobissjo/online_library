
from django.urls import path
from .views import BookRetrieveUpdateDeleteView, BookCreateListView, BorrowRequestApprovalView, BorrowRequestCreateListView


urlpatterns = [
    path('', BookCreateListView.as_view(), name='book-create'),
    path('<uuid:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
    #borrow request
    path('borrow-request/', BorrowRequestCreateListView.as_view(), 
         name='borrow-request-list-create'),
    #
    path('borrow-requests/approve/', BorrowRequestApprovalView.as_view(), 
         name='borrow-request-approval'),
    path('borrow-requests/approve/<uuid:borrow_request_id>/', BorrowRequestApprovalView.as_view(), 
         name='borrow-request-approve')
]