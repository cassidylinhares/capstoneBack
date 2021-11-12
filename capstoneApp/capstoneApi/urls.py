from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="ApiOverview"),
    path('getLights/', views.get_lights, name="getLights"),
    path('getLight/<str:pk>/', views.get_light, name="getLight"),
    path('insertLight/', views.insert_light, name="insertLight"),
    # path('updateLight/<str:pk>/', views.update_light, name="updateLight"),
    # path('deleteLight/<str:pk>/', views.delete_light, name="deleteLight"),
]