from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitor_list, name='visitor_list'),
    path('add/', views.add_visitor, name='add_visitor'),
    path('delete/<int:id>/', views.delete_visitor, name='delete_visitor'),
    path('edit/<int:id>/', views.edit_visitor, name='edit_visitor'),
]