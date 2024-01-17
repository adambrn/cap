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

    # Для EquipmentCategory
    path('equipmentcategory/list/', EquipmentCategoryListView.as_view(), name='equipmentcategory_list'),
    path('equipmentcategory/create/', EquipmentCategoryCreateView.as_view(), name='equipmentcategory_create'),
    path('equipmentcategory/<int:pk>/update/', EquipmentCategoryUpdateView.as_view(), name='equipmentcategory_update'),
    path('equipmentcategory/<int:pk>/detail/', EquipmentCategoryDetailView.as_view(), name='equipmentcategory_detail'),
    path('equipmentcategory/<int:pk>/delete/', EquipmentCategoryDeleteView.as_view(), name='equipmentcategory_delete'),

    # Для EquipmentStatus
    path('equipmentstatus/list/', EquipmentStatusListView.as_view(), name='equipmentstatus_list'),
    path('equipmentstatus/create/', EquipmentStatusCreateView.as_view(), name='equipmentstatus_create'),
    path('equipmentstatus/<int:pk>/update/', EquipmentStatusUpdateView.as_view(), name='equipmentstatus_update'),
    path('equipmentstatus/<int:pk>/detail/', EquipmentStatusDetailView.as_view(), name='equipmentstatus_detail'),
    path('equipmentstatus/<int:pk>/delete/', EquipmentStatusDeleteView.as_view(), name='equipmentstatus_delete'),

    # Для ComponentStatus
    path('componentstatus/list/', ComponentStatusListView.as_view(), name='componentstatus_list'),
    path('componentstatus/create/', ComponentStatusCreateView.as_view(), name='componentstatus_create'),
    path('componentstatus/<int:pk>/update/', ComponentStatusUpdateView.as_view(), name='componentstatus_update'),
    path('componentstatus/<int:pk>/detail/', ComponentStatusDetailView.as_view(), name='componentstatus_detail'),
    path('componentstatus/<int:pk>/delete/', ComponentStatusDeleteView.as_view(), name='componentstatus_delete'),

    # Для MemoryType
    path('memorytype/list/', MemoryTypeListView.as_view(), name='memorytype_list'),
    path('memorytype/create/', MemoryTypeCreateView.as_view(), name='memorytype_create'),
    path('memorytype/<int:pk>/update/', MemoryTypeUpdateView.as_view(), name='memorytype_update'),
    path('memorytype/<int:pk>/detail/', MemoryTypeDetailView.as_view(), name='memorytype_detail'),
    path('memorytype/<int:pk>/delete/', MemoryTypeDeleteView.as_view(), name='memorytype_delete'),

    # Для StorageType
    path('storagetype/list/', StorageTypeListView.as_view(), name='storagetype_list'),
    path('storagetype/create/', StorageTypeCreateView.as_view(), name='storagetype_create'),
    path('storagetype/<int:pk>/update/', StorageTypeUpdateView.as_view(), name='storagetype_update'),
    path('storagetype/<int:pk>/detail/', StorageTypeDetailView.as_view(), name='storagetype_detail'),
    path('storagetype/<int:pk>/delete/', StorageTypeDeleteView.as_view(), name='storagetype_delete'),

    # Для SocketType
    path('sockettype/list/', SocketTypeListView.as_view(), name='sockettype_list'),
    path('sockettype/create/', SocketTypeCreateView.as_view(), name='sockettype_create'),
    path('sockettype/<int:pk>/update/', SocketTypeUpdateView.as_view(), name='sockettype_update'),
    path('sockettype/<int:pk>/detail/', SocketTypeDetailView.as_view(), name='sockettype_detail'),
    path('sockettype/<int:pk>/delete/', SocketTypeDeleteView.as_view(), name='sockettype_delete'),
    ]
