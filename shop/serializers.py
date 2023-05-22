from rest_framework import serializers
from .models import Product, ProductInventory, Category, Discount

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'updated_at')

class CategoryInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'updated_at')


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'updated_at')

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ('id', 'created_at', 'updated_at')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategorySerializer(instance.category).data
        data["inventory"] = CategorySerializer(instance.category).data
        data["discount"] = DiscountSerializer(instance.discount).data
        return data