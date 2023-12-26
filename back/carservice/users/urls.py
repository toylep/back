from django.urls import path
from users.views import UserCreateView, UserSingleView, UserGetView, UserListView

urlpatterns = [
    path("list/", UserListView.as_view()),
    path("<int:pk>", UserSingleView.as_view()),
    path("get/<str:username>", UserGetView.as_view()),
    path("reg/", UserCreateView.as_view()),
]
