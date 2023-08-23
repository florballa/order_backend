from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Costumer
from .serializers import CostumerSerializer, UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]
    # authentication_classes = [IsAuthenticatedOrReadOnly]


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CostumerListCreateAPIView(ListCreateAPIView):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer


class CostumerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer
