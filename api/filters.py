from django_filters.rest_framework import FilterSet
from inventory.models import Item, Category

class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = {
            "name": ("exact", "iexact", "icontains"),
            "weight": ("exact", "gte", "lte"),
            "price": ("exact", "gte", "lte"),
            "quantity": ("exact", "gte", "lte"),
            "category": ("exact", "isnull"),
            "category__name": ("exact", "iexact", "icontains"),
        }


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            "name": ("exact", "iexact", "icontains"),
        }