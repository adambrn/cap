from django.urls import path
from components.views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'components'

urlpatterns = [
    path('', ComponentListView.as_view(), name='components'),
    #path('<str:model>/<int:pk>/', ComponentDetailView.as_view(), name='component_detail'),
    path('create/<str:component_type>/', CreateComponentView.as_view(), name='create_component'),
    
    path('create/', SelectComponentView.as_view(), name='select_component'),
    #Процессор
    path('processor_list/', ProcessorListView.as_view(), name='processor_list'), 
    path('processor/create', ProcessorCreateView.as_view(), name='processor_create'),
    path('processor/<int:pk>/update', ProcessorUpdateView.as_view(), name='processor_update'),
    path('processor/<int:pk>/delete', ProcessorDeleteView.as_view(), name='processor_delete'),
    path('processor/<int:pk>/detail', ProcessorDetailView.as_view(), name='processor_detail'), 
    #Материнская плата
    path('motherboard_list/', MotherboardListView.as_view(), name='motherboard_list'),
    path('motherboard/create', MotherboardCreateView.as_view(), name='motherboard_create'),
    path('motherboard/<int:pk>/update', MotherboardUpdateView.as_view(), name='motherboard_update'),
    path('motherboard/<int:pk>/delete', MotherboardDeleteView.as_view(), name='motherboard_delete'),
    path('motherboard/<int:pk>/detail', MotherboardDetailView.as_view(), name='motherboard_detail'), 
    #Память
    path('ram_list/', RAMListView.as_view(), name='ram_list'),
    path('ram/create', RAMCreateView.as_view(), name='ram_create'),
    path('ram/<int:pk>/update', RAMUpdateView.as_view(), name='ram_update'),
    path('ram/<int:pk>/delete', RAMDeleteView.as_view(), name='ram_delete'),
    path('ram/<int:pk>/detail', RAMDetailView.as_view(), name='ram_detail'), 
    
    #Видеокарта
    path('graphicscard_list/', GraphicsCardListView.as_view(), name='graphicscard_list'),  
    path('graphicscard/create', GraphicsCardCreateView.as_view(), name='graphicscard_create'),
    path('graphicscard/<int:pk>/update', GraphicsCardUpdateView.as_view(), name='graphicscard_update'),
    path('graphicscard/<int:pk>/delete', GraphicsCardDeleteView.as_view(), name='graphicscard_delete'),
    path('graphicscard_detail/<int:pk>/', GraphicsCardDetailView.as_view(), name='graphicscard_detail'),

    #Жесткий диск
    path('storage_list/', StorageListView.as_view(), name='storage_list'),
    path('storage_detail/<int:pk>/', StorageDetailView.as_view(), name='storage_detail'), 
    path('storage/create', StorageCreateView.as_view(), name='storage_create'),
    path('storage/<int:pk>/update', StorageUpdateView.as_view(), name='storage_update'),
    path('storage/<int:pk>/delete', StorageDeleteView.as_view(), name='storage_delete'),  

    #Блок питания
    path('powersupply_list/', PowerSupplyListView.as_view(), name='powersupply_list'),
    path('powersupply_detail/<int:pk>/', PowerSupplyDetailView.as_view(), name='powersupply_detail'),
    path('powerSupply/create', PowerSupplyCreateView.as_view(), name='powersupply_create'),
    path('powerSupply/<int:pk>/update', PowerSupplyUpdateView.as_view(), name='powersupply_update'),
    path('powerSupply/<int:pk>/delete', PowerSupplyDeleteView.as_view(), name='powersupply_delete'), 

    #Охлаждение
    path('cooler_list/', CoolerListView.as_view(), name='cooler_list'),
    path('cooler_detail/<int:pk>/', CoolerDetailView.as_view(), name='cooler_detail'),
    path('cooler/create', CoolerCreateView.as_view(), name='cooler_create'),
    path('cooler/<int:pk>/update', CoolerUpdateView.as_view(), name='cooler_update'),
    path('cooler/<int:pk>/delete', CoolerDeleteView.as_view(), name='cooler_delete'), 

    #Корпус
    path('case_list/', CaseListView.as_view(), name='case_list'),
    path('case_detail/<int:pk>/', CaseDetailView.as_view(), name='case_detail'),
    path('case/create', CaseCreateView.as_view(), name='case_create'),
    path('case/<int:pk>/update', CaseUpdateView.as_view(), name='case_update'),
    path('case/<int:pk>/delete', CaseDeleteView.as_view(), name='case_delete'), 

    #Сетевая карта
    path('networkcard_list/', NetworkCardListView.as_view(), name='networkcard_list'),
    path('networkcard_detail/<int:pk>/', NetworkCardDetailView.as_view(), name='networkcard_detail'),
    path('networkcard/create', NetworkCardCreateView.as_view(), name='networkcard_create'),
    path('networkcard/<int:pk>/update', NetworkCardUpdateView.as_view(), name='networkcard_update'),
    path('networkcard/<int:pk>/delete', NetworkCardDeleteView.as_view(), name='networkcard_delete'), 

    #Прочие
    path('othercomponent_list/', OtherComponentListView.as_view(), name='othercomponent_list'),
    path('othercomponent_detail/<int:pk>/', OtherComponentDetailView.as_view(), name='othercomponent_detail'),
    path('othercomponent/create', OtherComponentCreateView.as_view(), name='othercomponent_create'),
    path('othercomponent/<int:pk>/update', OtherComponentUpdateView.as_view(), name='othercomponent_update'),
    path('othercomponent/<int:pk>/delete', OtherComponentDeleteView.as_view(), name='othercomponent_delete'), 
    ]