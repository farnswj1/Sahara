from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import UserCreateForm, UserUpdateForm


# Create your views here.
class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "users/list.html"
    model = User
    queryset = User.objects.filter(is_active=True)
    context_object_name = "users"

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UserDetailView(DetailView):
    template_name = "users/detail.html"
    model = User
    context_object_name = "user_"

    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.is_staff or (user == self.get_object())


class UserCreateView(CreateView):
    template_name = "users/register_or_login.html"
    model = User
    form_class = UserCreateForm


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = "users/update.html"
    context_object_name = "user_"
    form_class = UserUpdateForm

    def test_func(self):
        return self.request.user.is_superuser or (self.request.user == self.get_object())


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    context_object_name = "user_"

    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        user_ = self.get_object()
        user_.is_active = False
        user_.save()
        return redirect("users:list")


class UserLoginView(LoginView):
    template_name="users/register_or_login.html"


class UserLogoutView(LogoutView):
    pass