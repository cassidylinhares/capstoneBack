from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="ApiOverview"),
    # path('getItems/', views.get_items, name="getItems"),
    # path('getItem/<str:pk>/', views.get_item, name="getItem"),
    # path('insertItem/', views.insert_item, name="insertItem"),
    # path('updateItem/<str:pk>/', views.update_item, name="updateItem"),
    # path('deleteItem/<str:pk>/', views.delete_item, name="deleteItem"),
]