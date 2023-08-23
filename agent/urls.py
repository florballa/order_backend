from django.urls import path

from .views import CostumerListCreateAPIView, CostumerRetrieveUpdateDestroyAPIView, UserListCreateAPIView, \
    UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name="users"),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name="users"),
    path('costumers/', CostumerListCreateAPIView.as_view(), name="costumers"),
    path('costumers/<int:pk>/', CostumerRetrieveUpdateDestroyAPIView.as_view(), name="costumer"),
]
