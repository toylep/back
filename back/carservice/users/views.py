from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
)
from users.serializers import ExtentedUserSerializer
from users.models import ExtendedUser
from rest_framework.response import Response

# Create your views here.


class UserCreateView(CreateAPIView):
    """
    Создаем кастомного юзера
    """

    serializer_class = ExtentedUserSerializer
    queryset = ExtendedUser.objects.all()


class UserListView(ListAPIView):
    """
    Получаем список юзеров
    """

    queryset = ExtendedUser.objects.all()
    serializer_class = ExtentedUserSerializer


class UserSingleView(RetrieveUpdateDestroyAPIView):
    """
    Меняем удаляем получаем юзера
    """

    queryset = ExtendedUser.objects.all()
    serializer_class = ExtentedUserSerializer


class UserGetView(GenericAPIView):
    def get(self, request, username):
        user = ExtendedUser.objects.get(username=username)
        serializer = ExtentedUserSerializer(user)
        return Response(serializer.data)
