from django.urls import path
from .views import signup 
from .views import UserLoginView

urlpatterns = [
   # path('signup/', UserSignupView.as_view(), name='user_signup'),
    #path('signup/<int:pk>/', UserSignupDetailView.as_view(), name='user_signup_detail'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path("signup/", signup, name="signup"), 
]
