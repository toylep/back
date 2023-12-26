from django.urls import path
from cars.views import (
   CarListCreateView,
   CarSingleView,
   CategoryListView,
   RentCreateView,
   RentSingleView,
   RentsListByUserView
   
   )
urlpatterns = [
   path('',CarListCreateView.as_view(),name='car-list'),
   path('<int:pk>',CarSingleView.as_view()),
   path('category/',CategoryListView.as_view()),
   path('rent/<int:pk>',RentSingleView.as_view()),
   path('rent/',RentCreateView.as_view()),
   path('rent/user/<str:username>',RentsListByUserView.as_view())

]
