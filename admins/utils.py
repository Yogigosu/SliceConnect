import razorpay
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

from FDA.constants import (
    DEFAULT_PAGINATED_BY, DEFAULT_GET_ELIDED_PAGE_RANGE_ON_EACH_SIDE,
    DEFAULT_GET_ELIDED_PAGE_RANGE_ON_ENDS
)


class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except (EmptyPage, PageNotAnInteger) as e:  # pragma: no cover
            raise Http404 from e

 