from rest_framework import serializers
from carts.models import CartItems, Cart


 
class IncreaseQuantityOfCartItemSerializer(serializers.ModelSerializer):
    """Used for increasing cart items quantity for the :model:`carts.CartItems`.
    """
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItems
        fields = ['quantity', 'total', 'cart_total']
        read_only_fields = ('total', 'cart_total')

    def get_cart_total(self, obj):
        return str(obj.cart.total)

    def to_internal_value(self, data):
        """Overridden for saving quantity in the data.
        """
        cart_item = CartItems.objects.filter(item_id=self.context['pk'],
                                             cart__user_id=self.context['request'].user.id).first()
        data = data.copy()
        data['quantity'] = cart_item.quantity + 1
        return super(IncreaseQuantityOfCartItemSerializer, self).to_internal_value(data)


class DecreaseQuantityOfCartItemSerializer(serializers.ModelSerializer):
    """Used for decreasing cart items quantity for the :model:`carts.CartItems`.
    """
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItems
        fields = ['quantity', 'total', 'cart_total']
        read_only_fields = ('total', 'cart_total')

    def get_cart_total(self, obj):
        return str(obj.cart.total)

    def to_internal_value(self, data):
        """Overridden for saving quantity in the data.
        """
        cart_item = CartItems.objects.filter(item_id=self.context['pk'],
                                             cart__user_id=self.context['request'].user.id).first()
        data = data.copy()
        data['quantity'] = cart_item.quantity - 1
        return super(DecreaseQuantityOfCartItemSerializer, self).to_internal_value(data)
