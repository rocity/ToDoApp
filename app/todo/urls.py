from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.addTodo, name = 'add'),
    path('complete/<int:todo_id>', views.completeTodo, name = 'completeTodo'),
    path('delete', views.delete_completed, name = 'delete_completed'),
    path('deleteAll', views.delete_all, name = 'delete_all')
]
