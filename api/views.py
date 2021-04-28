from rest_framework.generics import ListAPIView, RetrieveAPIView
from inventory.models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from .filters import ItemFilter, CategoryFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ItemListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter


class ItemRetrieveAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer