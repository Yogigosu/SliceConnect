from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from FDA.constants import (
    AGENT_REGISTRATION_FORM_PAGE, AGENT_LIST_ACCEPTED_ORDERS_PAGE, AGENT_CURRENT_DELIVERIES_PAGE,
    AGENT_SEE_AVAILABLE_DELIVERIES_PAGE, AGENT_REVIEWS_PAGE, AGENT_DETAIL_ORDER_PAGE,
    AGENT_TIME_ENTRY_PAGE, AGENT_APPLICATION_STATUS_PAGE, AGENT_NOT_AVAILABLE_PAGE,
    AGENT_EARNING_PAGE, AGENT_GET_COORDINATES_PAGE, AGENT_PANEL_PAGE
)
 

class AllDeliveriesListView(LoginRequiredMixin, VerifiedAgentRequiredMixin, PermissionRequiredMixin, PaginationMixin,
                            ListView):
    """
    View for all accepted deliveries
    """
    permission_required = ['delivery_agent.view_acceptedorder']
    model = AcceptedOrder
    template_name = AGENT_LIST_ACCEPTED_ORDERS_PAGE
    context_object_name = 'orders'
    ordering = ['-id']
    paginator_class = CustomPaginator
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return AllDeliveryListService(
            request=self.request, model=self.model
        ).get_queryset(queryset=queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return AllDeliveryListService(request=self.request, model=self.model).get_context_data(context)

 

class UpdateDeliveryStatusAPIView(LoginRequiredMixin, PermissionRequiredMixin, VerifiedAgentRequiredMixin,
                                  AvailableAgentRequiredMixin, APIView):
    """
    desc: Update APIView for delivery status by agent
    perms: custom_id of order status
    """
    permission_required = ['orders.change_order']
    model = Order

    def post(self, request):
        response = UpdateDeliveryStatusService(
            request=self.request, model=self.model
        ).update_data()
        return Response(response, status=status.HTTP_200_OK)


class AllTimeEntriesListView(LoginRequiredMixin, VerifiedAgentRequiredMixin, PermissionRequiredMixin, PaginationMixin,
                             ListView):
    """
    description: ListView for time entries of agent
    """
    permission_required = ['delivery_agent.view_activationtime']
    template_name = AGENT_TIME_ENTRY_PAGE
    model = ActivationTime
    context_object_name = 'active_time_obj'
    ordering = ['-id']
    paginator_class = CustomPaginator
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return AllTimeEntriesService(
            request=self.request, model=self.model
        ).get_queryset(queryset=queryset)


class AgentApplicationStatusView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """
    description: Delivery Agent Application Status page, when agent is unverified.
    """
    permission_required = ['delivery_agent.view_document']
    template_name = AGENT_APPLICATION_STATUS_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return AgentApplicationStatusService.get_context_data(context=context, user=self.request.user)


class NotAvailableTemplateView(LoginRequiredMixin, TemplateView):
    """
    description: TemplateView for Delivery Agent Not Available
    """
    template_name = AGENT_NOT_AVAILABLE_PAGE


class AgentEarningListView(LoginRequiredMixin, VerifiedAgentRequiredMixin, PaginationMixin, ListView):
    template_name = AGENT_EARNING_PAGE
    model = OrderPayoutDetail
    context_object_name = 'orders'
    ordering = ['-id']
    paginator_class = CustomPaginator
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return AgentEarningService(
            request=self.request, model=self.model
        ).get_queryset(queryset=queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return AgentEarningService(request=self.request, model=self.model).get_context_data(context)


class GetCoordinates(LoginRequiredMixin, TemplateView):
    """
    description: TemplateView for Delivery Agent Not Available
    """
    template_name = AGENT_GET_COORDINATES_PAGE
