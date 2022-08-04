from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('weedList/', views.weedList, name='strains'),
    path('getWeedDescription/<int:id>', views.getWeedDescription, name='more'),
]   