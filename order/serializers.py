from datetime import datetime

from rest_framework import serializers

from .models import Order, OrderUnit, Counter


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ['product', 'amount']


class OrderSerializer(serializers.ModelSerializer):
    order_units = OrderUnitSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'code', 'code_year', 'date_registered', 'costumer', 'order_units']

    @staticmethod
    def get_order_units(order_obj):
        units = order_obj.order_units.all()
        return OrderUnitSerializer(units, many=True).data


class OrderWriteSerializer(serializers.ModelSerializer):
    order_units = OrderUnitSerializer(many=True)

    class Meta:
        model = Order
        fields = ['costumer', 'order_units']

    def create(self, validated_data):
        creator = self.context['request'].user
        validated_data['creator'] = creator

        counters = Counter.objects.all()
        if counters:
            counter_obj = counters.first()
            value = counter_obj.value + 1
            counter_obj.value = value
            code = value
            counter_obj.save()
        else:
            value = 1
            counter = Counter.objects.create(name='PO', value=value)
            counter.save()

        now = datetime.now()
        code_year = now.strftime('%y')

        validated_data['code'] = code
        validated_data['code_year'] = code_year

        order_units_list = validated_data.pop('order_units')
        order = Order(**validated_data)
        order.save()

        for element in order_units_list:
            order_unit = OrderUnit(order=order, product=element['product'],
                                   amount=element['amount'],
                                   price=0)
            order_unit.save()
        return order

    def update(self, instance, validated_data):
        pass


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ['name', 'value']
