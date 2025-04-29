from django.urls import path
from apps.users.views import UserListView, RegisterView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='user-register'),
]