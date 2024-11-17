
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from requests import Response, models
from rest_framework import filters

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.prefetch_related('positions').all()
    serializer_class = StockSerializer

    def get_queryset(self):
        product = self.kwargs['products']
        return Stock.objects.prefetch_related('positions').filter(position__product=product)
    #  ошибка     product = self.kwargs['products']
    # KeyError: 'products'
    # Но ведь аргумент передается через url
    # а фильтрация через DjangoFilterBackend просто выводила все магазины
