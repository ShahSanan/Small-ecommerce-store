from django.db import models

# Create your models here.
from django.db import models

class Checkout(models.Model):
    name = models.CharField(max_length=55)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=23)
    phone = models.CharField(max_length=10)
