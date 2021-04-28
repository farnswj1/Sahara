from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path('', views.ItemListView.as_view(), name="item_list"),
    path('new/', views.ItemCreateView.as_view(), name="item_create"),
    path('<int:pk>/', views.ItemDetailView.as_view(), name="item_detail"),
    path('<int:pk>/update/', views.ItemUpdateView.as_view(), name="item_update"),
    path('<int:pk>/delete/', views.ItemDeleteView.as_view(), name="item_delete"),
    path('categories/', views.CategoryListView.as_view(), name="category_list"),
    path('categories/new/', views.CategoryCreateView.as_view(), name="category_create"),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name="category_update"),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name="category_delete"),
]