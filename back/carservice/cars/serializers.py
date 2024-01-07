from rest_framework.serializers import ModelSerializer
from cars.models import (
    Car,
    Category,
    Rent
    )
from users.serializers import ExtentedUserSerializer


class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'



class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CarFullSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Car
        fields = '__all__'

class RentSerializer(ModelSerializer):
    car = CarSerializer()
    client = ExtentedUserSerializer()

    class Meta:
        model = Rent
        fields = '__all__'


class RentCreateSerializer(ModelSerializer):
    class Meta:
        model = Rent
        fields = [
            'client',
            'car',
            'cost',
        ]