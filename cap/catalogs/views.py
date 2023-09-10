from functools import cached_property
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .filters import *
from cap.mixins import *
from .tables import *
from .models import *
from .forms import *
from view_breadcrumbs import DetailBreadcrumbMixin, BaseBreadcrumbMixin, CreateBreadcrumbMixin, DeleteBreadcrumbMixin, UpdateBreadcrumbMixin
from view_breadcrumbs.generic.base import BaseModelBreadcrumbMixin
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from django.views.generic.base import TemplateView


class Index(BaseContextMixin, LoginView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

#Базовые классы справочников
class BaseCatalogView(BaseModelBreadcrumbMixin, BaseCatalogMixin, SingleTableMixin, FilterView):
 
    @cached_property
    def crumbs(self):
        return [("Справочники", reverse_lazy("catalogs:catalogs")), (self.model_name_title_plural, "/")]

class BaseCatalogDetailView(DetailBreadcrumbMixin, BaseCatalogMixin, DetailView):
    pass

class BaseCatalogDeleteView(DeleteBreadcrumbMixin, BaseCatalogMixin, DeleteView):
    pass

class BaseCatalogUpdateView(UpdateBreadcrumbMixin, BaseCatalogMixin, UpdateView):
    success_url = reverse_lazy()
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)

class BaseCatalogCreateView(CreateBreadcrumbMixin, BaseCatalogMixin, CreateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)


#Справочники все
class CatalogsListView(BaseBreadcrumbMixin, BaseCatalogMixin , MultiTableMixin, TemplateView):
    template_name = 'catalogs/catalogs.html'
    
    def get_tables(self):
        tables = [
            ManufacturerTable(Manufacturer.objects.all()),           
        ]
        return tables

    @cached_property
    def crumbs(self):
        return [("Справочники", "components/")]

#Производитель
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

#LOGIN
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