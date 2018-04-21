from django.urls import path

from demo import views


urlpatterns = [
	path('', views.index),
    path('categories/', views.all_categories, name="all_categories"),
    path('categories/<int:category_id>/detail/', views.category_detail, name="categories_detail"),
    path('products/', views.all_products, name="all_products"),
    path('products/<int:product_id>/detail/', views.product_detail, name="products_detail"),
    path('categories/new/', views.new_category, name="new_category"),
    path('categories/add/', views.add_category, name="add_category"),
    path('products/new/', views.new_product, name="new_product"),
    path('products/add/', views.add_product, name="add_product"),
    path('categories/<int:category_id>/change/', views.change_category, name="change_category"),
    path('categories/<int:category_id>/edit/', views.edit_category, name="edit_category"),
    path('products/<int:product_id>/change/', views.change_product, name="change_product"),
    path('products/<int:product_id>/edit/', views.edit_product, name="edit_product"),
    path('categories/<int:category_id>/delete/', views.delete_category, name="delete_category"),
    path('products/<int:product_id>/delete/', views.delete_product, name="delete_product"),
]