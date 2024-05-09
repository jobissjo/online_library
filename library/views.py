from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from .models import Book, BorrowRequest
from .serializers import BookSerializer, BorrowRequestSerializer
from rest_framework.permissions import  IsAdminUser,AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class BookCreateListView(ListCreateAPIView):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()


class BookRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

class BorrowRequestCreateListView(ListCreateAPIView):
    queryset = BorrowRequest.objects.all()
    serializer_class = BorrowRequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class BorrowRequestApprovalView(APIView):
    permission_classes = [IsAdminUser]


    def get(self, request):
        pending_requests = BorrowRequest.objects.filter(status='pending')
        serializer = BorrowRequestSerializer(pending_requests, many=True)

        return Response(serializer.data)
    
    def post(self, request, borrow_request_id):
        borrow_request = get_object_or_404(BorrowRequest, id=borrow_request_id)
        borrow_request.approve_request()
        return Response(status=status.HTTP_200_OK)