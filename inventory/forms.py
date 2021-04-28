from django.forms import ModelForm, ModelChoiceField
from .models import Item, Category

class ItemForm(ModelForm):
    category = ModelChoiceField(required=True, queryset=Category.objects.all())
    
    class Meta:
        model = Item
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"