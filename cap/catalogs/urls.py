from django.urls import path
from .views import *


app_name = 'catalogs'

urlpatterns = [
    path('', CatalogsListView.as_view(), name='catalogs'),
    path('manufacturer/list/', ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturer/create/', ManufacturerCreateView.as_view(), name='manufacturer_create'), 
    path('manufacturer/<int:pk>/update', ManufacturerUpdateView.as_view(), name='manufacturer_update'), 
    path('manufacturer/<int:pk>/detail', ManufacturerDetailView.as_view(), name='manufacturer_detail'), 
    path('manufacturer/<int:pk>/delete', ManufacturerDeleteView.as_view(), name='manufacturer_delete'), 
    ]
