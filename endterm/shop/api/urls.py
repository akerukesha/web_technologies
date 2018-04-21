from django.urls import path

from api import views


urlpatterns = [
	path('', views.index),
    path('categories/', views.all_categories),
    path('products/', views.all_products),
    path('categories/add/', views.add_category),
    path('products/add/', views.add_product),
    path('categories/edit/', views.edit_category),
    path('products/edit/', views.edit_product),
    path('categories/delete/', views.delete_category),
    path('products/delete/', views.delete_product),
]