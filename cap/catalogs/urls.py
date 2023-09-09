from django.urls import path
from .views import *


app_name = 'catalogs'

urlpatterns = [
    path('', CatalogsListView.as_view(), name='catalogs'),
    path('manufacturer_list/', ManufacturerListView.as_view(), name='manufacturer_list'), 
    ]
