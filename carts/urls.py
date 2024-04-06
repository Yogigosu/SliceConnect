from django.urls import path

from .views import CreateCartItemAPIView, IncreaseQuantityOfCartItemAPIView, DeleteCartItemAPIView, \
    DecreaseQuantityOfCartItemAPIView

urlpatterns = [
    path('create-item/', CreateCartItemAPIView.as_view(), name="create-cart-item"),
    path('increase-item-quantity/<int:pk>/', IncreaseQuantityOfCartItemAPIView.as_view(),
         name="increase-cart-item-quantity"),
 
]
