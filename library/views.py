# from rest_framework.viewsets import ModelViewSet
# from .models import Book
# from .serializers import BookSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser,AllowAny
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.authentication import SessionAuthentication

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     authentication_classes = [JWTAuthentication]

#     permission_classes = [IsAdminUser] 

#     permission_classes_by_action = {
#         'list': [AllowAny],  # Optional: require authentication for listing
#         'retrieve': [AllowAny],  # Optional: require authentication for retrieving
#         'create': [IsAdminUser],
#         'update': [IsAdminUser],
#         'partial_update': [IsAdminUser],
#         'destroy': [IsAdminUser],
#     }

#     def get_permissions(self):
#         try:
#             return self.permission_classes_by_action[self.action]
#         except KeyError:
#             return self.permission_classes
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication


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