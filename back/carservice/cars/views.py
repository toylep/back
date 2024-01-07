
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    CreateAPIView,
    ListAPIView
)
from cars.models import (
    Car,
    Category,
    Rent,
)
from cars.serializers import (
    CarFullSerializer,
    CarSerializer,
    CategorySerializer,
    RentCreateSerializer,
    RentSerializer,
)
from rest_framework.response import Response
from users.models import ExtendedUser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db import transaction
from rest_framework.exceptions import APIException


class CarByCategoryView(GenericAPIView):

    def get(self, request, pk):
        cars = Car.objects.filter(category=pk)
        return Response(CarSerializer(cars, many=True).data)


class CarCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarListView(ListAPIView):

    queryset = Car.objects.filter(rent__car=None)
    serializer_class = CarFullSerializer


class CarSingleView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RentListView(ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer


class RentSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer


class RentCreateView(CreateAPIView):
    serializer_class = RentCreateSerializer
    queryset = Rent.objects.all()

    def post(self, request):
        user = ExtendedUser.objects.get(pk=request.data['client'])
        with transaction.atomic():
            user.balance -= request.data['cost']
            if user.balance < 0:
                raise APIException("У вас недостаточно средств")
            user.save()
            return super().post(request)


class RentsListByUserView(GenericAPIView):
    def get(self, request, username):
        user = ExtendedUser.objects.get(username=username)
        rents = Rent.objects.filter(client=user)
        serializer = RentSerializer(rents, many=True)
        return Response(serializer.data)
