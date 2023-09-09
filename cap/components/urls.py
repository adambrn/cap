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
    path('ram_detail/<int:pk>/', RAMDetailView.as_view(), name='ram_detail'),

    path('graphicscard_list/', GraphicsCardListView.as_view(), name='graphicscard_list'),  
    path('graphicscard_detail/<int:pk>/', GraphicsCardDetailView.as_view(), name='graphicscard_detail'),

    path('storage_list/', StorageListView.as_view(), name='storage_list'),
    path('storage_detail/<int:pk>/', StorageDetailView.as_view(), name='storage_detail'),   

    path('powersupply_list/', PowerSupplyListView.as_view(), name='powersupply_list'),
    path('powersupply_detail/<int:pk>/', PowerSupplyDetailView.as_view(), name='powersupply_detail'),

    path('cooler_list/', CoolerListView.as_view(), name='cooler_list'),
    path('cooler_detail/<int:pk>/', CoolerDetailView.as_view(), name='cooler_detail'),

    path('case_list/', CaseListView.as_view(), name='case_list'),
    path('case_detail/<int:pk>/', CaseDetailView.as_view(), name='case_detail'),

    path('networkcard_list/', NetworkCardListView.as_view(), name='networkcard_list'),
    path('networkcard_detail/<int:pk>/', NetworkCardDetailView.as_view(), name='networkcard_detail'),
    ]