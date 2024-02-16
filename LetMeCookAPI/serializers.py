from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal
from .models import Category

class CategorySeializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']


class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
    category = CategorySeializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock','price_after_tax','category','category_id']

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)