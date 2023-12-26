
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    CreateAPIView,
)
from cars.models import (
    Car,
    Category,
    Rent,
)
from cars.serializers import (
    CarSerializer,
    CategorySerializer,
    RentCreateSerializer,
    RentSerializer,
)
from rest_framework.response import Response
from users.models import ExtendedUser
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CarListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarSingleView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
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
    queryset = Rent.objects.all()
    serializer_class = RentCreateSerializer


class RentsListByUserView(GenericAPIView):
    def get(self, request, username):
        user = ExtendedUser.objects.get(username=username)
        rents = Rent.objects.filter(client=user)
        serializer = RentSerializer(rents, many=True)
        return Response(serializer.data)
