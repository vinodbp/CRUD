from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Insert/', views.Insert, name="create"),
    path('select/', views.select, name='select'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
]
