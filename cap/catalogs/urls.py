from django.urls import path
from .views import ComponentListView, EquipmentCatalogView, ComputerComponentsView, ComponentDetailView

from django.conf.urls.static import static
from django.conf import settings

app_name = 'catalogs'

urlpatterns = [
    path('', EquipmentCatalogView.as_view(), name='equipment_catalog'),
    path('equipment/<int:pk>/components/', ComputerComponentsView.as_view(), name='equipment_components'),
    path('components/', ComponentListView.as_view(), name='components'),
    path('components/<str:model>/<int:pk>/', ComponentDetailView.as_view(), name='component_detail'),
    # Добавьте другие URL-маршруты вашего приложения "catalogs" здесь
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)