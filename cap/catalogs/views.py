from functools import cached_property
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .filters import *
from cap.mixins import *
from .tables import *
from .models import *
from .forms import *
from view_breadcrumbs import DetailBreadcrumbMixin, BaseBreadcrumbMixin, CreateBreadcrumbMixin, DeleteBreadcrumbMixin, \
    UpdateBreadcrumbMixin
from view_breadcrumbs.generic.base import BaseModelBreadcrumbMixin
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from django.views.generic.base import TemplateView
from django.db.models import Count


class Index(BaseContextMixin, LoginView, ListView):
    template_name = 'index.html'
    context_object_name = 'status_counts'

    def get_queryset(self):
        status_counts = dict()
        models = [Computer, Monitor, Printer, Phone, NetworkDevice, OtherEquipment]

        for model in models:
            counts = (
                model.objects
                .values('equipment_status__name')
                .annotate(count=Count('equipment_status'))
            )
            if counts:
                status_counts[model] = counts
        return status_counts


# Базовые классы справочников
class BaseCatalogView(BaseModelBreadcrumbMixin, BaseCatalogMixin, SingleTableMixin, FilterView):

    @cached_property
    def crumbs(self):
        return [("Справочники", reverse_lazy("catalogs:catalogs")), (self.model_name_title_plural, "/")]


class BaseCatalogDetailView(DetailBreadcrumbMixin, BaseCatalogMixin, DetailView):
    pass


class BaseCatalogDeleteView(DeleteBreadcrumbMixin, BaseCatalogMixin, DeleteView):
    pass


class BaseCatalogUpdateView(UpdateBreadcrumbMixin, BaseCatalogMixin, UpdateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""
        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name, })
        return super().get_context_data(**kwargs)


class BaseCatalogCreateView(CreateBreadcrumbMixin, BaseCatalogMixin, CreateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name, })
        return super().get_context_data(**kwargs)


# Справочники все
class CatalogsListView(BaseBreadcrumbMixin, BaseCatalogMixin, MultiTableMixin, TemplateView):
    template_name = 'catalogs/catalogs.html'

    def get_tables(self):
        tables = [
            ManufacturerTable(Manufacturer.objects.all()),
        ]
        return tables

    @cached_property
    def crumbs(self):
        return [("Справочники", "components/")]


# Производитель
class ManufacturerListView(BaseCatalogView):
    model = Manufacturer
    template_name = 'catalogs/manufacturer_list.html'
    table_class = ManufacturerTable
    filterset_class = CatalogsFilter


class ManufacturerDetailView(BaseCatalogDetailView):
    model = Manufacturer


class ManufacturerDeleteView(BaseCatalogDeleteView):
    model = Manufacturer


class ManufacturerCreateView(BaseCatalogCreateView):
    model = Manufacturer
    form_class = ManufacturerForm


class ManufacturerUpdateView(BaseCatalogUpdateView):
    model = Manufacturer
    form_class = ManufacturerForm


# Сотрудники
class EmployeeListView(BaseCatalogView):
    model = Employee
    template_name = 'catalogs/employee_list.html'
    table_class = EmployeeTable
    filterset_class = CatalogsFilter


class EmployeeDetailView(BaseCatalogDetailView):
    model = Employee


class EmployeeDeleteView(BaseCatalogDeleteView):
    model = Employee


class EmployeeCreateView(BaseCatalogCreateView):
    model = Employee
    form_class = EmployeeForm


class EmployeeUpdateView(BaseCatalogUpdateView):
    model = Employee
    form_class = EmployeeForm


# Местоположение
class LocationListView(BaseCatalogView):
    model = Location
    template_name = 'catalogs/location_list.html'
    table_class = LocationTable
    filterset_class = CatalogsFilter


class LocationDetailView(BaseCatalogDetailView):
    model = Location


class LocationDeleteView(BaseCatalogDeleteView):
    model = Location


class LocationCreateView(BaseCatalogCreateView):
    model = Location
    form_class = LocationForm


class LocationUpdateView(BaseCatalogUpdateView):
    model = Location
    form_class = LocationForm


# Статусы оборудования
class EquipmentCategoryListView(BaseCatalogView):
    model = EquipmentCategory
    template_name = 'catalogs/equipment_category_list.html'
    table_class = EquipmentCategoryTable
    filterset_class = CatalogsFilter


class EquipmentCategoryDetailView(BaseCatalogDetailView):
    model = EquipmentCategory


class EquipmentCategoryDeleteView(BaseCatalogDeleteView):
    model = EquipmentCategory


class EquipmentCategoryCreateView(BaseCatalogCreateView):
    model = EquipmentCategory
    form_class = EquipmentCategoryForm


class EquipmentCategoryUpdateView(BaseCatalogUpdateView):
    model = EquipmentCategory
    form_class = EquipmentCategoryForm


# Классы для остальных каталогов
class EquipmentStatusListView(BaseCatalogView):
    model = EquipmentStatus
    template_name = 'catalogs/equipment_status_list.html'
    table_class = EquipmentStatusTable
    filterset_class = CatalogsFilter


class EquipmentStatusDetailView(BaseCatalogDetailView):
    model = EquipmentStatus


class EquipmentStatusDeleteView(BaseCatalogDeleteView):
    model = EquipmentStatus


class EquipmentStatusCreateView(BaseCatalogCreateView):
    model = EquipmentStatus
    form_class = EquipmentStatusForm


class EquipmentStatusUpdateView(BaseCatalogUpdateView):
    model = EquipmentStatus
    form_class = EquipmentStatusForm


class ComponentStatusListView(BaseCatalogView):
    model = ComponentStatus
    template_name = 'catalogs/component_status_list.html'
    table_class = ComponentStatusTable
    filterset_class = CatalogsFilter


class ComponentStatusDetailView(BaseCatalogDetailView):
    model = ComponentStatus


class ComponentStatusDeleteView(BaseCatalogDeleteView):
    model = ComponentStatus


class ComponentStatusCreateView(BaseCatalogCreateView):
    model = ComponentStatus
    form_class = ComponentStatusForm


class ComponentStatusUpdateView(BaseCatalogUpdateView):
    model = ComponentStatus
    form_class = ComponentStatusForm


class MemoryTypeListView(BaseCatalogView):
    model = MemoryType
    template_name = 'catalogs/memory_type_list.html'
    table_class = MemoryTypeTable
    filterset_class = CatalogsFilter


class MemoryTypeDetailView(BaseCatalogDetailView):
    model = MemoryType


class MemoryTypeDeleteView(BaseCatalogDeleteView):
    model = MemoryType


class MemoryTypeCreateView(BaseCatalogCreateView):
    model = MemoryType
    form_class = MemoryTypeForm


class MemoryTypeUpdateView(BaseCatalogUpdateView):
    model = MemoryType
    form_class = MemoryTypeForm


class StorageTypeListView(BaseCatalogView):
    model = StorageType
    template_name = 'catalogs/storage_type_list.html'
    table_class = StorageTypeTable
    filterset_class = CatalogsFilter


class StorageTypeDetailView(BaseCatalogDetailView):
    model = StorageType


class StorageTypeDeleteView(BaseCatalogDeleteView):
    model = StorageType


class StorageTypeCreateView(BaseCatalogCreateView):
    model = StorageType
    form_class = StorageTypeForm


class StorageTypeUpdateView(BaseCatalogUpdateView):
    model = StorageType
    form_class = StorageTypeForm


class SocketTypeListView(BaseCatalogView):
    model = SocketType
    template_name = 'catalogs/socket_type_list.html'
    table_class = SocketTypeTable
    filterset_class = CatalogsFilter


class SocketTypeDetailView(BaseCatalogDetailView):
    model = SocketType


class SocketTypeDeleteView(BaseCatalogDeleteView):
    model = SocketType


class SocketTypeCreateView(BaseCatalogCreateView):
    model = SocketType
    form_class = SocketTypeForm


class SocketTypeUpdateView(BaseCatalogUpdateView):
    model = SocketType
    form_class = SocketTypeForm


# LOGIN
class BaseLoginView(BaseContextMixin, LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context


class BaseLogoutView(BaseContextMixin, LogoutView):
    template_name = 'accounts/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выход'
        return context
