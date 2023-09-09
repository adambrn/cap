from django import template

register = template.Library()

@register.simple_tag()
def model_verbose_name(model): 
    return model._meta.verbose_name





