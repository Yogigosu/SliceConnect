import razorpay
from django.contrib import messages

from FDA.constants import CANNOT_BLOCK_RESTAURANT_ERROR, CONTACT_NOT_CREATED_ERROR, FUND_NOT_CREATED_ERROR
from accounts.models import User
from admins.utils import create_razorpay_contact, create_fund_account
from delivery_agent.models import AgentCashEntry
from orders.models import Order, choice_status, OrderItems
from orders.services import client
from restaurant.models import Restaurant
import logging

logger = logging.getLogger('info_log')


class HomeService:
    @staticmethod
    def get_context_data(context):
        context.update(
            {
                'total_orders': Order.get_orders_count(),
                'total_delivered_orders': Order.get_delivered_orders_count(),
                'total_price': Order.get_total_of_all_orders(),

                'total_customers': User.get_total_customers_count(),
                'deactive_customers': User.get_blocked_customers_count(),
                'active_customers': User.get_active_customers_count(),
                'unverified_customers': User.get_inactive_customers_count(),

                'total_restaurants': Restaurant.get_total_restaurants_count(),
                'deactive_restaurants': Restaurant.get_blocked_restaurants_count(),
                'active_restaurants': Restaurant.get_active_restaurants_count(),
                'unverified_restaurants': Restaurant.get_restaurant_applications_count(),
 
            }
        )
        return context


class DriversListService:
    def __init__(self, request, model):
        self.request = request
        self.model = model

 


class DriversApplicationListService:
    def __init__(self, request, model):
        self.request = request
        self.model = model

    def get_queryset(self, queryset):
        queryset = self.model.get_unverified_agents(queryset=queryset)

        if params := self.request.GET.get('agent'):
            queryset = self.model.get_agent_with_search_params(params, queryset)

        return queryset


class DriversDetailService:
    @staticmethod
    def get_context_data(context, pk):
        context.update({'agent_user': User.get_user_from_id(pk=pk, queryset=User.get_total_agents())})
        return context


 


class UsersDetailService:
    @staticmethod
    def get_context_data(context, pk):
        context.update({'user_obj': User.get_user_from_id(pk=pk, queryset=User.get_total_customers())})
        return context


class RestaurantListService:
    def __init__(self, request, model):
        self.request = request
        self.model = model

    def get_queryset(self, queryset):
        queryset = self.model.get_total_restaurants(queryset=queryset)

        if params := self.request.GET.get('restaurant_search'):
            queryset = self.model.get_restaurant_with_search_params(params, queryset)
 

        return queryset


class RestaurantsDetailService:
    @staticmethod
    def get_context_data(context, pk):
        context.update({'restaurant': Restaurant.get_restaurant_from_id(pk=pk, queryset=Restaurant.get_total_restaurants())})
        return context


class RestaurantApplicationListService:
 

    def get_queryset(self, queryset):
        queryset = self.model.get_restaurant_applications(queryset=queryset)

        if params := self.request.GET.get('restaurant_search'):
            queryset = self.model.get_restaurant_with_search_params(params, queryset)

        return queryset


class OrdersListService:
    def __init__(self, request, model):
        self.request = request
        self.model = model

    def get_queryset(self, queryset):
        queryset = self.model.get_orders()

 

        if params := self.request.GET.get('restaurant'):
            queryset = self.model.get_order_from_restaurant_id(params, queryset)

        return queryset

    @staticmethod
    def get_context_data(context):
        context.update({'order_status': choice_status})
        context.update({'restaurants': Restaurant.get_active_restaurants()})
        return context


class OrdersDetailService:
    @staticmethod
    def get_context_data(context, pk):
        context.update({'order': Order.get_object_from_pk(pk=pk)})
        context.update({'items': OrderItems.get_items_from_order_id(pk=pk)})
        return context


class UserActionService:
    @staticmethod
    def perform_restaurant_action(request, pk):
        restaurant_action = request.POST.get('restaurant_action')
        restaurant_obj = Restaurant.get_object_from_pk(pk=pk)
 
        elif restaurant_obj and restaurant_action == 'unblock' and restaurant_obj.is_blocked:
            restaurant_obj.is_blocked = False

        restaurant_obj.save()

    @staticmethod
    def perform_agent_action(request, pk):
        agent_action = request.POST.get('agent_action')
        agent_obj = User.get_object_from_pk(pk=pk)
 

        agent_obj.save()

    @staticmethod
    def perform_customer_action(request, pk):
        user_action = request.POST.get('user_action')
        user_obj = User.get_object_from_pk(pk=pk)
 

        user_obj.save()

    @staticmethod
    def perform_cod_agent_action(request, pk):
        User.get_orders_from_user_id(pk=pk).update(deposit=True)
        logger.info(f'Payment is collected from agent with User(id={pk})')

    @staticmethod
    def perform_agent_application_action(request, pk):
        is_agent_valid = request.POST.get('is_agent_valid')

        user = User.get_object_from_pk(pk=pk)
        document = user.document

        if is_agent_valid in ['0', '1'] and document.application_status == 'pending':
            if is_agent_valid == '1':
                document.is_verified = True
                document.application_status = 'approved'

                contact = create_razorpay_contact(
                    client=client,
                    name=f"agent{user.id}",
                    contact=str(user.mobile_number),
                    contact_type='vendor',
                    reference_id=f"{user.id} - delivery agent"
                )

 
                fund_account_id = fund_account.get('id')

                if not fund_account_id:
                    messages.error(request, FUND_NOT_CREATED_ERROR)
                    return

                document.razorpay_fund_account_id = fund_account_id
            elif is_agent_valid == '0':
                document.application_status = 'rejected'

            document.save()

    @staticmethod
    def perform_restaurant_application_action(request, pk):
        is_restaurant_valid = request.POST.get('is_restaurant_valid')

        restaurant = Restaurant.get_object_from_pk(pk=pk)

        if is_restaurant_valid in ['0', '1'] and restaurant.application_status == 'pending':
            if is_restaurant_valid == '1':
                restaurant.is_verified = True
                restaurant.application_status = 'approved'

                contact = create_razorpay_contact(
                    client=client,
                    name=f"restaurant{restaurant.owner.id}",
                    email=restaurant.owner.email,
                    contact=str(restaurant.owner.mobile_number),
                    contact_type='vendor',
                    reference_id=f"{restaurant.owner.id} - restaurant owner"
                )

                contact_id = contact.get('id')

                if not contact_id:
                    messages.error(request, CONTACT_NOT_CREATED_ERROR)
                    return

                restaurant.documents.razorpay_contact_id = contact_id

                fund_account = create_fund_account(
                    client=client,
                    contact_id=contact['id'],
                    user_name=f"restaurant{restaurant.owner.id}",
                    ifsc='RAZR0000001',
                    account_number=restaurant.documents.account_no
                )

                fund_account_id = fund_account.get('id')

                if not fund_account_id:
                    messages.error(request, FUND_NOT_CREATED_ERROR)
                    return

                restaurant.documents.razorpay_fund_account_id = fund_account_id
                restaurant.documents.save()

            elif is_restaurant_valid == '0':
                restaurant.application_status = 'rejected'
            restaurant.save()


 

 