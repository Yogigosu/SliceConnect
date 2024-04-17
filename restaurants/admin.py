from django.contrib import admin
from .models import Restaurant, ServiceTime, RestaurantReview
 
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(ServiceTime, ServiceTimeAdmin)
admin.site.register(RestaurantReview)