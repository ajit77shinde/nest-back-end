from django.urls import path
from users.views import RegisterUserView, LoginUserView, TestAuthentication

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', TestAuthentication.as_view(), name='granted '),
]