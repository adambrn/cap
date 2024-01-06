from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView
from .models import *
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import *
from cap.mixins import *
from .tables import *
from .forms import *
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from view_breadcrumbs import DetailBreadcrumbMixin, BaseBreadcrumbMixin, CreateBreadcrumbMixin, DeleteBreadcrumbMixin, UpdateBreadcrumbMixin
from view_breadcrumbs.generic.base import BaseModelBreadcrumbMixin
from django.utils.functional import cached_property
from django.views.generic import DetailView
from django.utils import timezone
class HistoryView(View):
    pass

#Базовые классы справочников
class BaseHistoryView(BaseModelBreadcrumbMixin, BaseHistoryMixin, SingleTableMixin, FilterView):
 
    @cached_property
    def crumbs(self):
        return [("История", reverse_lazy("history:history")), (self.model_name_title_plural, "/")]

class BaseHistoryDetailView(DetailBreadcrumbMixin, BaseHistoryMixin, DetailView):
    pass

class BaseHistoryDeleteView(DeleteBreadcrumbMixin, BaseHistoryMixin, DeleteView):
    pass

class BaseHistoryUpdateView(BaseModelBreadcrumbMixin, BaseHistoryMixin, UpdateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""
        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)
    
    
    @cached_property
    def crumbs(self):
        return [("История", reverse_lazy("history:history")), (self.model_name_title_plural, "/")]
    
class BaseHistoryCreateView(BaseModelBreadcrumbMixin, BaseHistoryMixin, CreateView):
    def get_context_data(self, **kwargs):
        """Add the models verbose name to the context dictionary."""

        kwargs.update({
            "model_verbose_name": self.form_class._meta.model._meta.verbose_name,})
        return super().get_context_data(**kwargs)
    
    
    @cached_property
    def crumbs(self):
        return [("История", reverse_lazy("history:history")), (self.model_name_title_plural, "/")]

#Компьютеры
class ComputerHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = ComputerHistoryTable
    model = ComputerHistory
    template_name = 'history/computer_history_list.html'

    def get_queryset(self):
        # получить компьютер по его pk
        computer = get_object_or_404(Computer, pk=self.kwargs['equipment_pk'])
       
        # получить все записи истории перемещения связанные с этим компьютером
        qs = self.model.objects.filter(computer=computer)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        computer = get_object_or_404(Computer, pk=self.kwargs['equipment_pk'])
        context['computer'] = computer.name
        return context
    
    @cached_property
    def crumbs(self):
        computer = get_object_or_404(Computer, pk=self.kwargs['equipment_pk'])
        return [("История", reverse_lazy("history:history")), 
                (computer.name, reverse("equipments:computer_detail", kwargs={"pk": computer.pk})), 
                (self.model_name_title_plural, "/")]
    
class EmployeeComputerHistoryUpdateView(BaseHistoryUpdateView):
    model = ComputerHistory
    form_class = EmployeeComputerHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.employee = current_entry.employee
            history_entry.save()
            
            computer = history_entry.computer
            employee = Employee.objects.get(name = form.cleaned_data['employee'])
            location = history_entry.location
            start_date = timezone.now()  

            ComputerHistory.objects.create(computer=computer, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date)
            
            return super().form_valid(form)
    
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:computer_detail", kwargs={"pk": int(pk)})

class EmployeeComputerHistoryCreateView(BaseHistoryCreateView):
    model = ComputerHistory
    form_class = EmployeeComputerHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.computer = Computer.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.employee = form.cleaned_data['employee']
            history_entry.save()
        
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:computer_detail", kwargs={"pk": int(pk)})
    
class LocationComputerHistoryUpdateView(BaseHistoryUpdateView):
    model = ComputerHistory
    form_class = LocationComputerHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.location = current_entry.location
            history_entry.save()
            
            computer = history_entry.computer
            location = Location.objects.get(name = form.cleaned_data['location'])
            employee = history_entry.employee
            start_date = timezone.now()  

            ComputerHistory.objects.create(computer=computer, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date)
            
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:computer_detail", kwargs={"pk": int(pk)})
    
class LocationComputerHistoryCreateView(BaseHistoryCreateView):
    model = ComputerHistory
    form_class = LocationComputerHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.computer = Computer.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.location = form.cleaned_data['location']
            history_entry.save()
        
            return super().form_valid(form)
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:computer_detail", kwargs={"pk": int(pk)})

class LocationComputerHistoryClearView(View):
    
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(ComputerHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        computer = history_entry.computer
        employee = history_entry.employee

        #новая запись в ComputerHistory
        ComputerHistory.objects.create(
            computer=computer,
            employee=employee,
            start_date=timezone.now(),
            location=None
        )

        return redirect('equipments:computer_detail', pk=equipment_pk)

class EmployeeComputerHistoryClearView(View):
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(ComputerHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        computer = history_entry.computer
        location = history_entry.location

        #новая запись в ComputerHistory
        ComputerHistory.objects.create(
            computer=computer,
            employee=None,
            start_date=timezone.now(),
            location=location
        )

        return redirect('equipments:computer_detail', pk=equipment_pk)

#принтеры
class PrinterHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = PrinterHistoryTable
    model = PrinterHistory
    template_name = 'history/printer_history_list.html'

    def get_queryset(self):
        printer = get_object_or_404(Printer, pk=self.kwargs['equipment_pk'])
        qs = self.model.objects.filter(printer=printer)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        printer = get_object_or_404(Printer, pk=self.kwargs['equipment_pk'])
        context['printer'] = printer.name
        return context

class EmployeePrinterHistoryUpdateView(BaseHistoryUpdateView):
    model = PrinterHistory
    form_class = EmployeePrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
        current_entry = self.get_object()
        history_entry = form.save(commit=False)
        history_entry.end_date = timezone.now() 
        history_entry.employee = current_entry.employee
        history_entry.save()
        
        printer = history_entry.printer
        employee = Employee.objects.get(name=form.cleaned_data['employee'])
        location = history_entry.location
        start_date = timezone.now()  

        PrinterHistory.objects.create(printer=printer, 
                                      employee=employee, 
                                      location=location, 
                                      start_date=start_date)
        
        return super().form_valid(form)

class LocationPrinterHistoryUpdateView(BaseHistoryUpdateView):
    model = PrinterHistory
    form_class = LocationPrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
        current_entry = self.get_object()
        history_entry = form.save(commit=False)
        history_entry.end_date = timezone.now() 
        history_entry.location = current_entry.location
        history_entry.save()
        
        printer = history_entry.printer
        location = Location.objects.get(name=form.cleaned_data['location'])
        employee = history_entry.employee
        start_date = timezone.now()  

        PrinterHistory.objects.create(printer=printer, 
                                      employee=employee, 
                                      location=location, 
                                      start_date=start_date)
        
        return super().form_valid(form)

class EmployeePrinterHistoryCreateView(BaseHistoryCreateView):
    model = PrinterHistory
    form_class = EmployeePrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
        pk = self.kwargs['equipment_pk']
        history_entry = form.save(commit=False)
        history_entry.printer = Printer.objects.get(pk=pk)
        history_entry.start_date = timezone.now() 
        history_entry.employee = form.cleaned_data['employee']
        history_entry.save()
    
        return super().form_valid(form)

class LocationPrinterHistoryCreateView(BaseHistoryCreateView):
    model = PrinterHistory
    form_class = LocationPrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
        pk = self.kwargs['equipment_pk']
        history_entry = form.save(commit=False)
        history_entry.printer = Printer.objects.get(pk=pk)
        history_entry.start_date = timezone.now() 
        history_entry.location = form.cleaned_data['location']
        history_entry.save()
    

#мониторы  
