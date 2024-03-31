from django.urls import path

from .views import (
    AdminPanel, DriversListView ,
    DriversApplicationListView, UsersListView, UsersDetailView,
    RestaurantListView ,ActionForCodDeliveryAgentView
)

urlpatterns = [
    path('', AdminPanel.as_view(), name="admin-home"),
    path('drivers/', DriversListView.as_view(), name="drivers-list"),
    path('cod-agents/', CodAgentListView.as_view(), name="cod-agents-list"),
    path('drivers/application/', DriversApplicationListView.as_view(), name="drivers-list-application"),
 
    path('users/', UsersListView.as_view(), name="users-list"),
    path('users/<int:pk>/', UsersDetailView.as_view(), name="users-detail"),

    path('restaurants/', RestaurantListView.as_view(), name="restaurant-list"),
 
]
