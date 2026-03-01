from django.urls import path
from .views import follow_user, unfollow_user, RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
        path('follow/<int:user_id>/', follow_user),

    path('unfollow/<int:user_id>/', unfollow_user),
]