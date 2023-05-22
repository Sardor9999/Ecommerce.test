from django.shortcuts import get_object_or_404
from .models import Category, ProductInventory, Discount, Product
from .serializers import CategorySerializer, ProductInventorySerializer, DiscountSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


class CategoryListCreateAPIView(APIView):

    def get(self, request):
        cats = Category.objects.all()
        serializer = CategorySerializer(instance=cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(instance=instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        instance = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = get_object_or_404(Category, pk=pk)
        instance.delete()
        return Response({}, status=status.HTTP_404_NOT_FOUND)

class InventoryListCreateAPIView(ListCreateAPIView):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class InventorRetriveUpdatedestroyAPIView(RetrieveAPIView):
    """Product inventory detail, update and delete"""
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    lookup_field = "pk"

class DiscountListCreateAPIView(ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    lookup_field = "pk"

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"