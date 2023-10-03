from django.urls import path
from . import views


urlpatterns = [
    path('',views.profile,name='profile'),
    path('download/<str:fileuuid>/',views.download,name='download'),
]