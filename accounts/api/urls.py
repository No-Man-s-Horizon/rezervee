from django.urls import path
from accounts.api.views.create_view import CreateUserView
from accounts.api.views.retrieve_view import ProfileView
from accounts.api.views.update_views import UpdatePassword


app_name = "accounts"


urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
    path('change-password', UpdatePassword.as_view(), name='change-password'),
    path('register', CreateUserView.as_view(), name='register'),
]
