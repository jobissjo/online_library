from django.urls import path, include
from .views import UserSignInView, UserSignUpView,get_user_info


urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('signin/', UserSignInView.as_view(), name='signin'),
    path('current_user/', get_user_info, name='current_user'),
    path('api-auth/', include('rest_framework.urls'))

]