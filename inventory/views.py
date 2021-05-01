from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .mixins import UserIsAdminOrStaffMixin
from django.urls import reverse_lazy
from .models import Item, Category
from .forms import ItemForm, CategoryForm
from .filters import ItemFilter, CategoryFilter

# Create your views here.
class ItemListView(FilterView):
    template_name = "items/list.html"
    context_object_name = "items"
    filterset_class = ItemFilter
    paginate_by = 10


class ItemDetailView(DetailView):
    template_name = "items/detail.html"
    model = Item
    context_object_name = "item"


class ItemCreateView(UserIsAdminOrStaffMixin, CreateView):
    template_name = "items/new.html"
    model = Item
    form_class = ItemForm


class ItemUpdateView(UserIsAdminOrStaffMixin, UpdateView):
    template_name = "items/update.html"
    model = Item
    form_class = ItemForm


class ItemDeleteView(UserIsAdminOrStaffMixin, DeleteView):
    template_name = "items/delete.html"
    model = Item
    success_url = reverse_lazy("inventory:item_list")


class CategoryListView(UserIsAdminOrStaffMixin, FilterView):
    template_name = "categories/list.html"
    context_object_name = "categories"
    filterset_class = CategoryFilter
    paginate_by = 10


class CategoryCreateView(UserIsAdminOrStaffMixin, CreateView):
    template_name = "categories/new_or_update.html"
    model = Category
    form_class = CategoryForm


class CategoryUpdateView(UserIsAdminOrStaffMixin, UpdateView):
    template_name = "categories/new_or_update.html"
    model = Category
    form_class = CategoryForm


class CategoryDeleteView(UserIsAdminOrStaffMixin, DeleteView):
    template_name = "categories/delete.html"
    model = Category
    success_url = reverse_lazy("inventory:category_list")