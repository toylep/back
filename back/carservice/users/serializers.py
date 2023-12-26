from rest_framework.serializers import ModelSerializer
from users.models import ExtendedUser


class ExtentedUserSerializer(ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = [
            "id",
            "username",
            "first_name",
            "email",
            "is_staff",
            "balance",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
