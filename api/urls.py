from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("items/", views.ItemListAPIView.as_view(), name="item_list"),
    path("items/<int:pk>/", views.ItemRetrieveAPIView.as_view(), name="item_detail"),
    path("categories/", views.CategoryListAPIView.as_view(), name="category_list"),
    path("categories/<int:pk>/", views.CategoryRetrieveAPIView.as_view(), name="category_detail"),
]