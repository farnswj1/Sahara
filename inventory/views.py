from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Item, Category
from .forms import ItemForm, CategoryForm

# Create your views here.
class ItemListView(ListView):
    template_name = "items/list.html"
    model = Item
    context_object_name = "items"


class ItemDetailView(DetailView):
    template_name = "items/detail.html"
    model = Item
    context_object_name = "item"


class ItemCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "items/new.html"
    model = Item
    form_class = ItemForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "items/update.html"
    model = Item
    form_class = ItemForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "items/delete.html"
    model = Item
    success_url = reverse_lazy("inventory:item_list")

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class CategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "categories/list.html"
    model = Category
    context_object_name = "categories"

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "categories/new_or_update.html"
    model = Category
    form_class = CategoryForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "categories/new_or_update.html"
    model = Category
    form_class = CategoryForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "categories/delete.html"
    model = Category
    success_url = reverse_lazy("inventory:category_list")

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff