from django.urls import path
from history.views import *

app_name = 'history'

urlpatterns = [
    path('', HistoryView.as_view(), name='history'),
    path('computer/<int:computer_pk>', ComputerHistoryListView.as_view(), name='computer_history_list'),
    path('computer/<int:computer_pk>/employee_update/<int:pk>', EmployeeComputerHistoryUpdateView.as_view(), name='computer_history_employee_update'),
    path('computer/<int:computer_pk>/location_update/<int:pk>', LocationComputerHistoryUpdateView.as_view(), name='computer_history_location_update'),
]
