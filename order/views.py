from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Order, OrderUnit
from .serializers import OrderSerializer, OrderUnitSerializer, OrderWriteSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderSerializer
    write_serializer_class = OrderWriteSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'GET':
            return self.read_serializer_class
        return self.write_serializer_class


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUnitListCreateAPIView(ListCreateAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer


class OrderUnitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer
