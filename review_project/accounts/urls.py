from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterView, UserProfileView, UserChangeUpdateView, UserPasswordChangeView

app_name = "accounts"
urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', UserChangeUpdateView.as_view(), name='profile_update'),
    path('user/<int:pk>/password/change/', UserPasswordChangeView.as_view(), name='password_change'),

]
