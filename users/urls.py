from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verification_user, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verification/<int:user_pk>/', verification_user, name='verification'),
    # path('recovery_password/', PasswordResetView.as_view(template_name='users/password_reset.html'),
    #      name='recovery_password'),
    path('profile/generate_new_password/', generate_new_password, name='generate_new_password')
]