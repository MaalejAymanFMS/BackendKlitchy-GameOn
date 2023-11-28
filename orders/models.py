from django.db import models
from rest_framework import serializers

class Order(models.Model):
    order_id = models.CharField(primary_key=True,max_length=255)
    status_kds=models.CharField(max_length=255)
# Create your models here.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'