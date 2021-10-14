from django.urls import path

from user.views import SignUp, LoginView

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/login', LoginView.as_view()),
]
