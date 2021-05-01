from django_filters import FilterSet, CharFilter, BooleanFilter
from .models import User

class UserFilter(FilterSet):
    username = CharFilter("username", label="Username", lookup_expr="icontains")
    first_name = CharFilter("first_name", label="First name", lookup_expr="icontains")
    last_name = CharFilter("last_name", label="Last name", lookup_expr="icontains")
    email = CharFilter("email", label="Email", lookup_expr="icontains")
    is_staff = BooleanFilter("is_staff", label="Staff")
    is_superuser = BooleanFilter("is_superuser", label="Administrator")
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "is_staff", "is_superuser")