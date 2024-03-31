from django.conf import settings
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404

 
from restaurant.models import Restaurant


class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is admin user."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin or not request.user.groups.filter(name=USER_TYPES[3]).exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PkValidationMixin(AccessMixin):
    """Verify that the current pk is valid."""

    def dispatch(self, request, *args, **kwargs):
        if not self.class_name.get_object_from_pk(pk=kwargs['pk']):
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class DriverApplicationValidationMixin(AccessMixin):
    """Verify that current driver is having application."""

    def dispatch(self, request, *args, **kwargs):
        if not User.is_unverified_agent(pk=kwargs['pk']):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

 

 