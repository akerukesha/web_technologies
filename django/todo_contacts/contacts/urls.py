from django.urls import path

from contacts import views


urlpatterns = [
	path('', views.index),
    path('contact_list/', views.contact_list),
    path('contact_detail/<int:contact_id>/', views.contact_detail, name="contact_detail"),
    path('contact_add/', views.contact_add),
    path('contact_change/', views.contact_change),
    path('contact_delete/', views.contact_delete),
]