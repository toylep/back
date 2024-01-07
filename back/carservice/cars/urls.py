from django.urls import path
from cars.views import (
    CarCreateView,
    CarSingleView,
    CategoryListView,
    RentCreateView,
    RentSingleView,
    RentsListByUserView,
    CarByCategoryView,
    CarListView,
)

urlpatterns = [
    path("", CarCreateView.as_view(), name="car-list"),
    path("list/", CarListView.as_view(), name="car-add"),
    path("<int:pk>", CarSingleView.as_view()),
    path("category/", CategoryListView.as_view()),
    path("rent/<int:pk>", RentSingleView.as_view()),
    path("rent/", RentCreateView.as_view()),
    path("rent/user/<str:username>", RentsListByUserView.as_view()),
    path("category/<int:pk>", CarByCategoryView.as_view()),
]
