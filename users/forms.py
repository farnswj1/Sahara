from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username", "password1", "password2", "first_name", "last_name", 
            "email", "phone_number", "street_address", "city", "state", "zipcode"
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "email", "phone_number", 
            "street_address", "city", "state", "zipcode"
        )


class UserAdminUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "email", "phone_number", 
            "street_address", "city", "state", "zipcode", "is_superuser", "is_staff"
        )