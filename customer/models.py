from django.db import models
from seller.models import *
# Create your models here.
class CustomerRegistration(models.Model):
    Name=models.TextField(max_length=100,null=True)
    Email=models.TextField(max_length=100,null=True)
    Password=models.TextField(max_length=100,null=True)


class Cart(models.Model):
    customer=models.ForeignKey(CustomerRegistration,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)