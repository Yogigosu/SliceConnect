from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, TemplateView

 
from accounts.models import User
from admins.mixins import AdminRequiredMixin, PaginationMixin, PkValidationMixin, DriverApplicationValidationMixin, \
    RestaurantApplicationValidationMixin
from admins.services import (
    HomeService,
    DriversListService,
 
)
from admins.utils import CustomPaginator
from orders.models import Order
from restaurant.models import Restaurant


 
class DriversListView(LoginRequiredMixin, AdminRequiredMixin, PaginationMixin, ListView):
    model = User
    template_name = ADMINS_DRIVERS_LIST_PAGE
    context_object_name = 'drivers'
    ordering = ['-id']
    paginator_class = CustomPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        return DriversListService(request=self.request, model=self.model).get_queryset(queryset=queryset)


 
 
class CodAgentListView(LoginRequiredMixin, AdminRequiredMixin, PaginationMixin, ListView):
    model = User
    template_name = ADMINS_COD_AGENTS_LIST_PAGE
    context_object_name = 'agents'
    ordering = ['-id']
    paginator_class = CustomPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        return CodAgentListService(request=self.request, model=self.model).get_queryset(queryset=queryset)

 
class ActionForCodDeliveryAgentView(LoginRequiredMixin, AdminRequiredMixin, PkValidationMixin, View):
    class_name = User

    def post(self, request, pk):
        UserActionService.perform_cod_agent_action(request, pk)
        return redirect('cod-agents-list')
