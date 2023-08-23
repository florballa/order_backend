from django.urls import path
from .views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView, OrderUnitListCreateAPIView, \
    OrderUnitRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name="orders"),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name="order"),
    path('order-units/', OrderUnitListCreateAPIView.as_view(), name="order_units"),
    path('order-units/<int:pk>/', OrderUnitRetrieveUpdateDestroyAPIView.as_view(), name="order_unit"),
]
