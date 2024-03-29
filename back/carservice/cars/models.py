from django.db import models
# Create your models here.
import datetime
from django.utils import timezone
from users.models import ExtendedUser


class Category(models.Model):
    """Категория авто
    """
    name = models.CharField(max_length=50)
    price = models.FloatField()


class Car(models.Model):
    """Модель машины
    """
    picture = models.ImageField(upload_to='assets')
    model = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        )


class Rent(models.Model):
    """Модель аренды
    """
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(to=ExtendedUser, on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        auto_now_add=True,
        )
    end_date = models.DateTimeField(
        default=timezone.now()+datetime.timedelta(days=30)
        )
    cost = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
