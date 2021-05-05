from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import UserCreateForm, UserUpdateForm, UserAdminUpdateForm
from .filters import UserFilter


# Create your views here.
class UserListView(UserPassesTestMixin, FilterView):
    template_name = "users/list.html"
    queryset = User.objects.filter(is_active=True)
    context_object_name = "users"
    filterset_class = UserFilter
    paginate_by = 15
    extra_context = {"title": "List of Accounts"}

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UserDetailView(DetailView):
    template_name = "users/detail.html"
    model = User
    context_object_name = "user_"
    extra_context = {"title": "Account Information"}

    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.is_staff or (user == self.get_object())


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "users/register_or_login.html"
    model = User
    form_class = UserCreateForm
    success_message = "Your account was created successfully!"
    extra_context = {"title": "Register"}


class UserUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = "users/update.html"
    context_object_name = "user_"
    success_message = "The account was updated successfully!"
    extra_context = {"title": "Update Account"}

    def test_func(self):
        return self.request.user.is_superuser or (self.request.user == self.get_object())
    
    def get_form_class(self):
        user = self.request.user
        user_ = self.get_object()
        return UserAdminUpdateForm if user.is_superuser and user != user_ else UserUpdateForm
    
    def get_success_url(self):
        return reverse("users:list")


class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    context_object_name = "user_"
    success_message = "The account was deleted successfully!"
    extra_context = {"title": "Delete Account"}

    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        user_ = self.get_object()
        user_.is_active = False
        user_.save()
        messages.success(self.request, self.success_message)
        return redirect("users:list")


class UserLoginView(LoginView):
    template_name="users/register_or_login.html"
    extra_context = {"title": "Login"}


class UserLogoutView(LogoutView):
    pass