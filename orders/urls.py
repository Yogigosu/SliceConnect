from django.urls import re_path
from . import views
app_name = 'orders'

urlpatterns = [
	re_path(r'^cart-add/$', views.addToCart_view, name='cart-add'),
	re_path(r'^check-discount/$', views.checkDiscountCode_view, name='check-discount'),
	re_path(r"^mylist/$", views.myOrders_view, name='mylist'),
 	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/$', views.OrderDetail_view, name='detail'),
	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/delete/$', views.DeleteOrder_view, name='delete' ),
	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/update-status/$', views.updateStatus_view, name='update-status' ),
 
]