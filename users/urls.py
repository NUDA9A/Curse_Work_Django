from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, RegisterView, ProfileView, verify_user, UsersListView, UserManagerView

app_name = UsersConfig.name
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/confirm/<str:verify_code>/', verify_user, name='verify_user'),
    path('manage/<int:pk>', UserManagerView.as_view(), name='manage'),
]
