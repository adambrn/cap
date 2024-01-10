from django.views.generic.base import ContextMixin

menu = [
  {'title': 'Главная', 'url': '/'},
  {'title': 'О компании', 'url': '/about'},
  {'title': 'Контакты', 'url': '/contacts'},
  {'title': 'Каталог', 'url': '/catalog'}
]
class BaseContextMixin(ContextMixin):

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['menu'] = menu
    return context