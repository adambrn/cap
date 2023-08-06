from django.views import View
from django.shortcuts import render
from .models import Equipment, Motherboard, Processor, RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard

components_name = [Motherboard, Processor, RAM, GraphicsCard, Storage, PowerSupply, Cooler, Case, NetworkCard]
class EquipmentCatalogView(View):
    template_name = 'catalog.html'

    def get(self, request, *args, **kwargs):
        equipment_list = Equipment.objects.all()
        return render(request, self.template_name, {'equipment_list': equipment_list})

class EquipmentComponentsView(View):
    template_name = 'equipment_components.html'

    def get(self, request, equipment_id, *args, **kwargs):
        try:
            equipment = Equipment.objects.get(id=equipment_id)
            components = []

            # Получаем все компоненты для данного оборудования
            for component_class in components_name:
                try:
                    component = component_class.objects.get(equipment=equipment)
                    components.append(component)
                except component_class.DoesNotExist:
                    pass

            context = {
                'equipment': equipment,
                'components': components,
            }
            return render(request, self.template_name, context)
        except Equipment.DoesNotExist:
            # Оборудование не найдено, обработайте эту ситуацию по вашему усмотрению
            pass