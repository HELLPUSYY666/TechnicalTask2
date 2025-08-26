from rest_framework import serializers

from .models import Product


class ProductTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock", "created_at"]
