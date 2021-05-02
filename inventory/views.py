from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .mixins import UserIsAdminOrStaffMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Item, Category
from .forms import ItemForm, CategoryForm
from .filters import ItemFilter, CategoryFilter

# Create your views here.
class ItemListView(FilterView):
    template_name = "items/list.html"
    context_object_name = "items"
    filterset_class = ItemFilter
    paginate_by = 15


class ItemDetailView(DetailView):
    template_name = "items/detail.html"
    model = Item
    context_object_name = "item"


class ItemCreateView(UserIsAdminOrStaffMixin, SuccessMessageMixin, CreateView):
    template_name = "items/new.html"
    model = Item
    form_class = ItemForm
    success_message = "The item was created successfully!"


class ItemUpdateView(UserIsAdminOrStaffMixin, SuccessMessageMixin, UpdateView):
    template_name = "items/update.html"
    model = Item
    form_class = ItemForm
    success_message = "The item was updated successfully!"


class ItemDeleteView(UserIsAdminOrStaffMixin, DeleteView):
    template_name = "items/delete.html"
    model = Item
    success_url = reverse_lazy("inventory:item_list")
    success_message = "The item was deleted successfully!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()


class CategoryListView(UserIsAdminOrStaffMixin, FilterView):
    template_name = "categories/list.html"
    context_object_name = "categories"
    filterset_class = CategoryFilter
    paginate_by = 15


class CategoryCreateView(UserIsAdminOrStaffMixin, SuccessMessageMixin, CreateView):
    template_name = "categories/new_or_update.html"
    model = Category
    form_class = CategoryForm
    success_message = "The category was created successfully!"


class CategoryUpdateView(UserIsAdminOrStaffMixin, SuccessMessageMixin, UpdateView):
    template_name = "categories/new_or_update.html"
    model = Category
    form_class = CategoryForm
    success_message = "The category was updated successfully!"


class CategoryDeleteView(UserIsAdminOrStaffMixin, DeleteView):
    template_name = "categories/delete.html"
    model = Category
    success_url = reverse_lazy("inventory:category_list")
    success_message = "The category was deleted successfully!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()