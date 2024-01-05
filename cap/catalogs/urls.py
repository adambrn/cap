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
    
    path('employee/list/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee_create'), 
    path('employee/<int:pk>/update', EmployeeUpdateView.as_view(), name='employee_update'), 
    path('employee/<int:pk>/detail', EmployeeDetailView.as_view(), name='employee_detail'), 
    path('employee/<int:pk>/delete', EmployeeDeleteView.as_view(), name='employee_delete'), 

    path('location/list/', LocationListView.as_view(), name='location_list'),
    path('location/create/', LocationCreateView.as_view(), name='location_create'), 
    path('location/<int:pk>/update', LocationUpdateView.as_view(), name='location_update'), 
    path('location/<int:pk>/detail', LocationDetailView.as_view(), name='location_detail'), 
    path('location/<int:pk>/delete', LocationDeleteView.as_view(), name='location_delete'), 
    ]
