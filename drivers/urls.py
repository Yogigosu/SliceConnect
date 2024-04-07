from django.urls import path

from delivery_agent.views import (
    UpdateAgentStatusAPIView, RegisterDeliveryAgent, AgentPanelView,
    AllDeliveriesListView,
)

urlpatterns = [
    path("register/", RegisterDeliveryAgent.as_view(), name="register-delivery-agent"),
    path("panel/", AgentPanelView.as_view(), name="delivery-agent-panel"),
    path("update-status/", UpdateAgentStatusAPIView.as_view(), name="update_agent_status"),
    path("see_available_deliveries/", SeeAvailableDeliveriesListView.as_view(), name="see-available-deliveries"),
    path("accept_delivery/", AcceptDeliveryAPIView.as_view(), name="accept_delivery"),
    path("agent_review/<int:pk>/", SeeAllRatingAndReviewsView.as_view(), name="agent_review"),
    path("all_delivery/", AllDeliveriesListView.as_view(), name="all-accepted-delivery"),
 
    path("get_coordinates/", GetCoordinates.as_view(), name="get-coordinates"),
]
