from django.urls import path
from shop.views import CategoryListCreateAPIView, CategoryDetailUpdateDeleteView, InventoryListCreateAPIView, InventorRetriveUpdatedestroyAPIView, DiscountListCreateAPIView, DiscountRetrieveUpdateDestroyAPIView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyView
urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name="cat_list_create"),
    path('category/<int:pk>/', CategoryDetailUpdateDeleteView.as_view(), name="cat-detail-views"),
    path('inventory/',InventoryListCreateAPIView.as_view(), name='product_inventory'),
    path('inventory/<int:pk>/', InventorRetriveUpdatedestroyAPIView.as_view(), name='inventory-detail-view'),
    path('discount/', DiscountListCreateAPIView.as_view(), name="discount-list-create-view"),
    path('discount/<int:pk>', DiscountRetrieveUpdateDestroyAPIView.as_view(), name="discount-list-create-view"),
    path('product/', ProductListCreateAPIView.as_view(), name="product-list-view"),
    path('product/<int:pk>/',ProductRetrieveUpdateDestroyView.as_view(), name="product-detail-view")
]