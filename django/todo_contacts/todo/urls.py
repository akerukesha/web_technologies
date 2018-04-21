from django.urls import path

from todo import views


urlpatterns = [
	path('', views.index),
    path('todo_list/', views.todo_list),
    path('todo_detail/<int:todo_id>/', views.todo_detail, name="todo_detail"),
    path('todo_add/', views.todo_add),
    path('todo_done/', views.todo_done),
    path('todo_delete/', views.todo_delete),
]
