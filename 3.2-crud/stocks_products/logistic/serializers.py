from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ('id', 'product', 'quantity', 'price')

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ('id', 'address', 'positions')

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            StockProduct.objects.update(stock=stock, **position)

        return stock

        # обновляется все по последнему значению, что характерно, ведь обновление идет каждый цикл на текущий position
        # пробовала https://stackoverflow.com/questions/68443223/django-rest-framework-update-nested-serializer-by-id


        #stock = (instance.positions)(all)
        #stock = list(positions)
        #for position in positions:
        #    stock_item=stock.pop(0)
        #    stock_item.quantity = position.get('quantity', stock_item.quantity)
        #    stock_item.price = position.get('price', stock_item.price)
        #    stock_item.save()
        #return instance

        # TypeError: __call__() takes 1 positional argument but 2 were given






