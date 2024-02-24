
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    CreateAPIView,
    ListAPIView
)
from rest_framework.pagination import PageNumberPagination
from cars.models import (
    Car,
    Category,
    Rent,
)
from django_filters import rest_framework as filters
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
from django.http import FileResponse


class CarPagination(PageNumberPagination):

    page_size = 7
    page_query_param = 'page'


class CarCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarListView(ListAPIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = CarPagination
    queryset = Car.objects.filter(rent__car=None).order_by('id')
    serializer_class = CarFullSerializer


class CarSingleView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class CategorySingleView(RetrieveUpdateDestroyAPIView):
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


class PictureExport(GenericAPIView):
    
    def get(self, request, filename):
        img = open(f'assets/{filename}', 'rb')
        return FileResponse(img)
