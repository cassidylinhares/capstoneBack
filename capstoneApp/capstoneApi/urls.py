from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="ApiOverview"),
    path('getLights/<str:room>/', views.get_lights, name="getLights"),
    path('getLight/<str:room>/', views.get_light, name="getLight"),
    path('setLight/<str:room>/<str:cmd>/', views.set_light, name="setLight"),
    path('insertLight/', views.insert_light, name="insertLight"),
    # path('updateLight/<str:pk>/', views.update_light, name="updateLight"),
    # path('deleteLight/<str:pk>/', views.delete_light, name="deleteLight"),

    path('getTemps/', views.get_temps, name="getTemps"),
    path('getTemp/<str:time>/', views.get_light, name="getTemp"),
    path('setTemp/<str:temp>/', views.set_temp, name="setTemp"),
    path('insertTemp/', views.insert_temp, name="insertTemp"),
]