from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
 

from .models import CartItems
from .serializers import (
    CreateCartItemSerializer
)
from .services import IncreaseQuantityOfCartItemServices, DecreaseQuantityOfCartItemService, DeleteCartItemService

 

class DecreaseQuantityOfCartItemAPIView(LoginRequiredMixin, PermissionRequiredMixin, APIView):
    """Decrease Quantity for :model:`carts.CartItems`.
    """
    permission_required = ['carts.change_cartitems']

    def post(self, request, pk, *args, **kwargs):
        return DecreaseQuantityOfCartItemService.decrease_quantity_of_cart_item(request=request, pk=pk)


class DeleteCartItemAPIView(LoginRequiredMixin, PermissionRequiredMixin, APIView):
    """Delete method for :model:`carts.CartItems`.
    """
    permission_required = ['carts.delete_cartitems']

    def post(self, request, pk, *args, **kwargs):
        return DeleteCartItemService.delete_cart_item(request=request, pk=pk)
