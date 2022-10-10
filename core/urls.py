from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('all/',TodoListView.as_view(),name='all_todos'),
    path('add/',TodoCreateView.as_view(),name='add_todo'),
    path('todo/<int:pk>/',TodoDetailView.as_view(),name='todo_detail'),
    path('edit/<int:pk>/',TodoUpdate.as_view(),name='update_todo'),
    path('delete/<int:pk>/',TodoDelete.as_view(),name='delete_todo'),

]