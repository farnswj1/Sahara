from django_filters import FilterSet, CharFilter, NumericRangeFilter, NumberFilter
from .models import Item, Category

class ItemFilter(FilterSet):
    name = CharFilter("name", label="Name", lookup_expr="icontains")
    weight_min = NumberFilter("weight", label="Minimum weight", lookup_expr="gte")
    weight_max = NumberFilter("weight", label="Maximum weight", lookup_expr="lte")
    price_min = NumberFilter("price", label="Minimum price", lookup_expr="gte")
    price_max = NumberFilter("price", label="Maximum price", lookup_expr="lte")
    quantity_min = NumberFilter("quantity", label="Minimum quantity", lookup_expr="gte")
    quantity_max = NumberFilter("quantity", label="Maximum quantity", lookup_expr="lte")

    class Meta:
        model = Item
        fields = (
            "id", "name", "category", "weight_min", "weight_max", 
            "price_min", "price_max", "quantity_min", "quantity_max"
        )


class CategoryFilter(FilterSet):
    name = CharFilter("name", label="Name", lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ("id", "name",)