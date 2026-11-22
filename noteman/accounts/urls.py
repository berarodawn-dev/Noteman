from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup' ),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('delete_note/<int:note_id>', views.delete_note, name='delete_note'),
    path('home/create_note', views.create_note, name='create_note'),
    path('home/create_task', views.create_task, name="create_task"),
    path('home/delete_task/<int:task_id>', views.delete_task, name="delete_task")
]
 