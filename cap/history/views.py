from django.apps import apps
from django.views.generic.base import TemplateView
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
class AllComputerHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = ComputerHistoryTable
    model = ComputerHistory
    template_name = 'history/equipment_history_list.html'   

class ComputerHistoryListView(AllComputerHistoryListView):
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
                                           start_date=start_date,
                                           user = self.request.user)
            
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
            history_entry.user = self.request.user
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
            history_entry.user = self.request.user
            history_entry.location = current_entry.location
            history_entry.save()
            
            computer = history_entry.computer
            location = Location.objects.get(name = form.cleaned_data['location'])
            employee = history_entry.employee
            start_date = timezone.now()  

            ComputerHistory.objects.create(computer=computer, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user,)
            
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
            history_entry.user = self.request.user
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
            user = self.request.user,
            location=None,
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
            location=location,
            user = self.request.user,
        )

        return redirect('equipments:computer_detail', pk=equipment_pk)

#принтеры
class AllPrinterHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = PrinterHistoryTable
    model = PrinterHistory
    template_name = 'history/equipment_history_list.html'   

class PrinterHistoryListView(AllPrinterHistoryListView):
    template_name = 'history/printer_history_list.html'

    def get_queryset(self):
        # получить компьютер по его pk
        printer = get_object_or_404(Printer, pk=self.kwargs['equipment_pk'])
       
        # получить все записи истории перемещения связанные с этим компьютером
        qs = self.model.objects.filter(printer=printer)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        printer = get_object_or_404(Printer, pk=self.kwargs['equipment_pk'])
        context['printer'] = printer.name
        return context
    
    @cached_property
    def crumbs(self):
        printer = get_object_or_404(Printer, pk=self.kwargs['equipment_pk'])
        return [("История", reverse_lazy("history:history")), 
                (printer.name, reverse("equipments:printer_detail", kwargs={"pk": printer.pk})), 
                (self.model_name_title_plural, "/")]

class EmployeePrinterHistoryUpdateView(BaseHistoryUpdateView):
    model = PrinterHistory
    form_class = EmployeePrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.employee = current_entry.employee
            history_entry.user = self.request.user
            history_entry.save()
            
            printer = history_entry.printer
            employee = Employee.objects.get(name = form.cleaned_data['employee'])
            location = history_entry.location
            start_date = timezone.now()  

            PrinterHistory.objects.create(printer=printer, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)
    
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:printer_detail", kwargs={"pk": int(pk)})

class EmployeePrinterHistoryCreateView(BaseHistoryCreateView):
    model = PrinterHistory
    form_class = EmployeePrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.printer = Printer.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.employee = form.cleaned_data['employee']
            history_entry.user = self.request.user
            history_entry.save()
        
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:printer_detail", kwargs={"pk": int(pk)})
    
class LocationPrinterHistoryUpdateView(BaseHistoryUpdateView):
    model = PrinterHistory
    form_class = LocationPrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.location = current_entry.location
            history_entry.user = self.request.user
            history_entry.save()
            
            printer = history_entry.printer
            location = Location.objects.get(name = form.cleaned_data['location'])
            employee = history_entry.employee
            start_date = timezone.now()  

            PrinterHistory.objects.create(printer=printer, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:printer_detail", kwargs={"pk": int(pk)})
    
class LocationPrinterHistoryCreateView(BaseHistoryCreateView):
    model = PrinterHistory
    form_class = LocationPrinterHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.printer = Printer.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.user = self.request.user
            history_entry.location = form.cleaned_data['location']
            history_entry.save()
        
            return super().form_valid(form)
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:printer_detail", kwargs={"pk": int(pk)})

class LocationPrinterHistoryClearView(View):
    
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(PrinterHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        printer = history_entry.printer
        employee = history_entry.employee

        #новая запись в PrinterHistory
        PrinterHistory.objects.create(
            printer=printer,
            employee=employee,
            start_date=timezone.now(),
            user = self.request.user,
            location=None
        )

        return redirect('equipments:printer_detail', pk=equipment_pk)

class EmployeePrinterHistoryClearView(View):
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(PrinterHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        printer = history_entry.printer
        location = history_entry.location

        #новая запись в PrinterHistory
        PrinterHistory.objects.create(
            printer=printer,
            employee=None,
            start_date=timezone.now(),
            location=location,
            user = self.request.user
        )

        return redirect('equipments:printer_detail', pk=equipment_pk)


#мониторы 
class AllMonitorHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = MonitorHistoryTable
    model = MonitorHistory
    template_name = 'history/equipment_history_list.html'   

class MonitorHistoryListView(AllMonitorHistoryListView):
    template_name = 'history/monitor_history_list.html'

    def get_queryset(self):
        # получить компьютер по его pk
        monitor = get_object_or_404(Monitor, pk=self.kwargs['equipment_pk'])
       
        # получить все записи истории перемещения связанные с этим компьютером
        qs = self.model.objects.filter(monitor=monitor)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        monitor = get_object_or_404(Monitor, pk=self.kwargs['equipment_pk'])
        context['monitor'] = monitor.name
        return context
    
    @cached_property
    def crumbs(self):
        monitor = get_object_or_404(Monitor, pk=self.kwargs['equipment_pk'])
        return [("История", reverse_lazy("history:history")), 
                (monitor.name, reverse("equipments:monitor_detail", kwargs={"pk": monitor.pk})), 
                (self.model_name_title_plural, "/")]

class EmployeeMonitorHistoryUpdateView(BaseHistoryUpdateView):
    model = MonitorHistory
    form_class = EmployeeMonitorHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.employee = current_entry.employee
            history_entry.user = self.request.user
            history_entry.save()
            
            monitor = history_entry.monitor
            employee = Employee.objects.get(name = form.cleaned_data['employee'])
            location = history_entry.location
            start_date = timezone.now()  

            MonitorHistory.objects.create(monitor=monitor, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)
    
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:monitor_detail", kwargs={"pk": int(pk)})

class EmployeeMonitorHistoryCreateView(BaseHistoryCreateView):
    model = MonitorHistory
    form_class = EmployeeMonitorHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.monitor = Monitor.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.employee = form.cleaned_data['employee']
            history_entry.user = self.request.user
            history_entry.save()
        
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:monitor_detail", kwargs={"pk": int(pk)})
    
class LocationMonitorHistoryUpdateView(BaseHistoryUpdateView):
    model = MonitorHistory
    form_class = LocationMonitorHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.location = current_entry.location
            history_entry.user = self.request.user
            history_entry.save()
            
            monitor = history_entry.monitor
            location = Location.objects.get(name = form.cleaned_data['location'])
            employee = history_entry.employee
            start_date = timezone.now()  

            MonitorHistory.objects.create(monitor=monitor, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:monitor_detail", kwargs={"pk": int(pk)})
    
class LocationMonitorHistoryCreateView(BaseHistoryCreateView):
    model = MonitorHistory
    form_class = LocationMonitorHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.monitor = Monitor.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.location = form.cleaned_data['location']
            history_entry.user = self.request.user
            history_entry.save()
        
            return super().form_valid(form)
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:monitor_detail", kwargs={"pk": int(pk)})

class LocationMonitorHistoryClearView(View):
    
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(MonitorHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        monitor = history_entry.monitor
        employee = history_entry.employee

        #новая запись в MonitorHistory
        MonitorHistory.objects.create(
            monitor=monitor,
            employee=employee,
            start_date=timezone.now(),
            location=None,
            user = self.request.user
        )

        return redirect('equipments:monitor_detail', pk=equipment_pk)

class EmployeeMonitorHistoryClearView(View):
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(MonitorHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        monitor = history_entry.monitor
        location = history_entry.location

        #новая запись в MonitorHistory
        MonitorHistory.objects.create(
            monitor=monitor,
            employee=None,
            start_date=timezone.now(),
            location=location,
            user = self.request.user
        )

        return redirect('equipments:monitor_detail', pk=equipment_pk)

#телефоны
class AllPhoneHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = PhoneHistoryTable
    model = PhoneHistory
    template_name = 'history/equipment_history_list.html'   

class PhoneHistoryListView(AllPhoneHistoryListView):
    template_name = 'history/phone_history_list.html'

    def get_queryset(self):
        # получить компьютер по его pk
        phone = get_object_or_404(Phone, pk=self.kwargs['equipment_pk'])
       
        # получить все записи истории перемещения связанные с этим компьютером
        qs = self.model.objects.filter(phone=phone)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phone = get_object_or_404(Phone, pk=self.kwargs['equipment_pk'])
        context['phone'] = phone.name
        return context
    
    @cached_property
    def crumbs(self):
        phone = get_object_or_404(Phone, pk=self.kwargs['equipment_pk'])
        return [("История", reverse_lazy("history:history")), 
                (phone.name, reverse("equipments:phone_detail", kwargs={"pk": phone.pk})), 
                (self.model_name_title_plural, "/")]

class EmployeePhoneHistoryUpdateView(BaseHistoryUpdateView):
    model = PhoneHistory
    form_class = EmployeePhoneHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.user = self.request.user
            history_entry.employee = current_entry.employee
            history_entry.save()
            
            phone = history_entry.phone
            employee = Employee.objects.get(name = form.cleaned_data['employee'])
            location = history_entry.location
            start_date = timezone.now()  

            PhoneHistory.objects.create(phone=phone, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)
    
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:phone_detail", kwargs={"pk": int(pk)})

class EmployeePhoneHistoryCreateView(BaseHistoryCreateView):
    model = PhoneHistory
    form_class = EmployeePhoneHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.phone = Phone.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.employee = form.cleaned_data['employee']
            history_entry.save()
        
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:phone_detail", kwargs={"pk": int(pk)})
    
class LocationPhoneHistoryUpdateView(BaseHistoryUpdateView):
    model = PhoneHistory
    form_class = LocationPhoneHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.user = self.request.user
            history_entry.location = current_entry.location
            history_entry.save()
            
            phone = history_entry.phone
            location = Location.objects.get(name = form.cleaned_data['location'])
            employee = history_entry.employee
            start_date = timezone.now()  

            PhoneHistory.objects.create(phone=phone, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:phone_detail", kwargs={"pk": int(pk)})
    
class LocationPhoneHistoryCreateView(BaseHistoryCreateView):
    model = PhoneHistory
    form_class = LocationPhoneHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.phone = Phone.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.location = form.cleaned_data['location']
            history_entry.save()
        
            return super().form_valid(form)
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:phone_detail", kwargs={"pk": int(pk)})

class LocationPhoneHistoryClearView(View):
    
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(PhoneHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        phone = history_entry.phone
        employee = history_entry.employee

        #новая запись в PhoneHistory
        PhoneHistory.objects.create(
            phone=phone,
            employee=employee,
            start_date=timezone.now(),
            location=None,
            user = self.request.user
        )

        return redirect('equipments:phone_detail', pk=equipment_pk)

class EmployeePhoneHistoryClearView(View):
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(PhoneHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        phone = history_entry.phone
        location = history_entry.location

        #новая запись в PhoneHistory
        PhoneHistory.objects.create(
            phone=phone,
            employee=None,
            start_date=timezone.now(),
            location=location,
            user = self.request.user
        )

        return redirect('equipments:phone_detail', pk=equipment_pk)
    
#сетевое
class AllNetworkDeviceHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = NetworkDeviceHistoryTable
    model = NetworkDeviceHistory
    template_name = 'history/equipment_history_list.html'   

class NetworkDeviceHistoryListView(AllNetworkDeviceHistoryListView):
    template_name = 'history/networkdevice_history_list.html'

    def get_queryset(self):
        # получить компьютер по его pk
        networkdevice = get_object_or_404(NetworkDevice, pk=self.kwargs['equipment_pk'])
       
        # получить все записи истории перемещения связанные с этим компьютером
        qs = self.model.objects.filter(networkdevice=networkdevice)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        networkdevice = get_object_or_404(NetworkDevice, pk=self.kwargs['equipment_pk'])
        context['networkdevice'] = networkdevice.name
        return context
    
    @cached_property
    def crumbs(self):
        networkdevice = get_object_or_404(NetworkDevice, pk=self.kwargs['equipment_pk'])
        return [("История", reverse_lazy("history:history")), 
                (networkdevice.name, reverse("equipments:networkdevice_detail", kwargs={"pk": networkdevice.pk})), 
                (self.model_name_title_plural, "/")]

class EmployeeNetworkDeviceHistoryUpdateView(BaseHistoryUpdateView):
    model = NetworkDeviceHistory
    form_class = EmployeeNetworkDeviceHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.user = self.request.user
            history_entry.employee = current_entry.employee
            history_entry.save()
            
            networkdevice = history_entry.networkdevice
            employee = Employee.objects.get(name = form.cleaned_data['employee'])
            location = history_entry.location
            start_date = timezone.now()  

            NetworkDeviceHistory.objects.create(networkdevice=networkdevice, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)
    
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:networkdevice_detail", kwargs={"pk": int(pk)})

class EmployeeNetworkDeviceHistoryCreateView(BaseHistoryCreateView):
    model = NetworkDeviceHistory
    form_class = EmployeeNetworkDeviceHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.networkdevice = NetworkDevice.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.employee = form.cleaned_data['employee']
            history_entry.save()
        
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:networkdevice_detail", kwargs={"pk": int(pk)})
    
class LocationNetworkDeviceHistoryUpdateView(BaseHistoryUpdateView):
    model = NetworkDeviceHistory
    form_class = LocationNetworkDeviceHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.user = self.request.user
            history_entry.location = current_entry.location
            history_entry.save()
            
            networkdevice = history_entry.networkdevice
            location = Location.objects.get(name = form.cleaned_data['location'])
            employee = history_entry.employee
            start_date = timezone.now()  

            NetworkDeviceHistory.objects.create(networkdevice=networkdevice, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:networkdevice_detail", kwargs={"pk": int(pk)})
    
class LocationNetworkDeviceHistoryCreateView(BaseHistoryCreateView):
    model = NetworkDeviceHistory
    form_class = LocationNetworkDeviceHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.networkdevice = NetworkDevice.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.location = form.cleaned_data['location']
            history_entry.save()
        
            return super().form_valid(form)
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:networkdevice_detail", kwargs={"pk": int(pk)})

class LocationNetworkDeviceHistoryClearView(View):
    
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(NetworkDeviceHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        networkdevice = history_entry.networkdevice
        employee = history_entry.employee

        #новая запись в NetworkDeviceHistory
        NetworkDeviceHistory.objects.create(
            networkdevice=networkdevice,
            employee=employee,
            start_date=timezone.now(),
            location=None,
            user = self.request.user
        )

        return redirect('equipments:networkdevice_detail', pk=equipment_pk)

class EmployeeNetworkDeviceHistoryClearView(View):
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(NetworkDeviceHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        networkdevice = history_entry.networkdevice
        location = history_entry.location

        #новая запись в NetworkDeviceHistory
        NetworkDeviceHistory.objects.create(
            networkdevice=networkdevice,
            employee=None,
            start_date=timezone.now(),
            location=location,
            user = self.request.user
        )

        return redirect('equipments:networkdevice_detail', pk=equipment_pk)
    
#другое
class AllOtherEquipmentHistoryListView(BaseHistoryView):
    filterset_class = HistoryFilter
    table_class = OtherEquipmentHistoryTable
    model = OtherEquipmentHistory
    template_name = 'history/equipment_history_list.html'   

class OtherEquipmentHistoryListView(AllOtherEquipmentHistoryListView):
    template_name = 'history/otherequipment_history_list.html'

    def get_queryset(self):
        # получить компьютер по его pk
        otherequipment = get_object_or_404(OtherEquipment, pk=self.kwargs['equipment_pk'])
       
        # получить все записи истории перемещения связанные с этим компьютером
        qs = self.model.objects.filter(otherequipment=otherequipment)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        otherequipment = get_object_or_404(OtherEquipment, pk=self.kwargs['equipment_pk'])
        context['otherequipment'] = otherequipment.name
        return context
    
    @cached_property
    def crumbs(self):
        otherequipment = get_object_or_404(OtherEquipment, pk=self.kwargs['equipment_pk'])
        return [("История", reverse_lazy("history:history")), 
                (otherequipment.name, reverse("equipments:otherequipment_detail", kwargs={"pk": otherequipment.pk})), 
                (self.model_name_title_plural, "/")]

class EmployeeOtherEquipmentHistoryUpdateView(BaseHistoryUpdateView):
    model = OtherEquipmentHistory
    form_class = EmployeeOtherEquipmentHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.user = self.request.user
            history_entry.employee = current_entry.employee
            history_entry.save()
            
            otherequipment = history_entry.otherequipment
            employee = Employee.objects.get(name = form.cleaned_data['employee'])
            location = history_entry.location
            start_date = timezone.now()  

            OtherEquipmentHistory.objects.create(otherequipment=otherequipment, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)
    
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:otherequipment_detail", kwargs={"pk": int(pk)})

class EmployeeOtherEquipmentHistoryCreateView(BaseHistoryCreateView):
    model = OtherEquipmentHistory
    form_class = EmployeeOtherEquipmentHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.otherequipment = OtherEquipment.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.employee = form.cleaned_data['employee']
            history_entry.save()
        
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:otherequipment_detail", kwargs={"pk": int(pk)})
    
class LocationOtherEquipmentHistoryUpdateView(BaseHistoryUpdateView):
    model = OtherEquipmentHistory
    form_class = LocationOtherEquipmentHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    
    def form_valid(self, form):
            current_entry = self.get_object()
            history_entry = form.save(commit=False)
            history_entry.end_date = timezone.now() 
            history_entry.user = self.request.user
            history_entry.location = current_entry.location
            history_entry.save()
            
            otherequipment = history_entry.otherequipment
            location = Location.objects.get(name = form.cleaned_data['location'])
            employee = history_entry.employee
            start_date = timezone.now()  

            OtherEquipmentHistory.objects.create(otherequipment=otherequipment, 
                                           employee=employee, 
                                           location=location, 
                                           start_date=start_date,
                                           user = self.request.user)
            
            return super().form_valid(form)

    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:otherequipment_detail", kwargs={"pk": int(pk)})
    
class LocationOtherEquipmentHistoryCreateView(BaseHistoryCreateView):
    model = OtherEquipmentHistory
    form_class = LocationOtherEquipmentHistoryForm
    template_name = 'history/equipment_history_employee_form.html'
    def form_valid(self, form):
            pk=self.kwargs['equipment_pk']
            
            history_entry = form.save(commit=False)
            history_entry.otherequipment = OtherEquipment.objects.get(pk=pk)
            history_entry.start_date = timezone.now() 
            history_entry.location = form.cleaned_data['location']
            history_entry.save()
        
            return super().form_valid(form)
    def get_success_url(self):
        pk=self.kwargs['equipment_pk']
        return reverse("equipments:otherequipment_detail", kwargs={"pk": int(pk)})

class LocationOtherEquipmentHistoryClearView(View):
    
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(OtherEquipmentHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        otherequipment = history_entry.otherequipment
        employee = history_entry.employee

        #новая запись в OtherEquipmentHistory
        OtherEquipmentHistory.objects.create(
            otherequipment=otherequipment,
            employee=employee,
            start_date=timezone.now(),
            location=None,
            user = self.request.user
        )

        return redirect('equipments:otherequipment_detail', pk=equipment_pk)

class EmployeeOtherEquipmentHistoryClearView(View):
    def get(self, request, pk, equipment_pk):
        
        history_entry = get_object_or_404(OtherEquipmentHistory, pk=pk)

        history_entry.end_date = timezone.now()
        history_entry.save()

        #компьютер и сотрудника из текущей записи
        otherequipment = history_entry.otherequipment
        location = history_entry.location

        #новая запись в OtherEquipmentHistory
        OtherEquipmentHistory.objects.create(
            otherequipment=otherequipment,
            employee=None,
            start_date=timezone.now(),
            location=location,
            user = self.request.user
        )

        return redirect('equipments:otherequipment_detail', pk=equipment_pk)
    
class ComponentHistoryListView(BaseBreadcrumbMixin,  BaseComponentMixin, SingleTableView):
    #filterset_class = HistoryFilter
    template_name = 'history/component_history_list.html'
    
    def get_queryset(self):
         
        component = self.kwargs['component']
        
        model_name = apps.get_model('components', component)
       
        component_name = model_name.__name__
        print(component_name)
        model = apps.get_model('history', f'{component_name}History')
        get_filter = {f'{component}_id':self.kwargs['pk']}
        queryset = model.objects.filter(**get_filter)
               

        return queryset
    
    def get_table_class(self):
        
        component = self.kwargs['component']
        TABLES_CLASS ={
             'processor': ProcessorHistoryTable,
             'motherboard': MotherboardHistoryTable,
             'ram': RAMHistoryTable,
             'storage': StorageHistoryTable,
             'graphicscard': GraphicsCardHistoryTable,
             'powersupply':PowerSupplyHistoryTable,
             'case':CaseHistoryTable,
             'cooler':CoolerHistoryTable,
             'othercomponent':OtherComponentHistoryTable,
             'networkcard':NetworkCardHistoryTable,

        }
        #table_class = apps.get_model('history', f'table.{component_name}HistoryTable')

        self.table_class = TABLES_CLASS[component]
                
        return super().get_table_class()
    
    @cached_property
    def crumbs(self):
        pk = self.kwargs['component']    
        model_name = apps.get_model('components', pk)
       
        component = model_name.__name__
        component_object = get_object_or_404(model_name, pk=self.kwargs['pk'])
        return [("Компоненты", reverse_lazy('components:components')),
                (component_object.name ,reverse_lazy(f'components:{pk}_detail', kwargs={'pk': self.kwargs['pk']})),
                (f"История компонента" , ''),
                ]
    
   
    
