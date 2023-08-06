from django.urls import path
from .views import EquipmentCatalogView, EquipmentComponentsView

app_name = 'catalogs'

urlpatterns = [
    path('', EquipmentCatalogView.as_view(), name='equipment_catalog'),
    path('equipment/<int:equipment_id>/components/', EquipmentComponentsView.as_view(), name='equipment_components'),
    # Добавьте другие URL-маршруты вашего приложения "catalogs" здесь
]
