from django import template

register = template.Library()

@register.simple_tag()
def model_verbose_name(model): 
    return model._meta.verbose_name

@register.filter
def get_model_name(self):
    return str(self.__class__.__name__).lower()



