from io import BytesIO
from math import sin, cos, sqrt, atan2, radians, ceil

from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa

from accounts.tasks import send_mail_task


def send_otp_email(email, otp, order_id):
    context = {
        'subject': 'Confirm Order Otp',
        'otp': otp,
        'order_id': order_id
    }
    send_mail(email, 'confirm_order_otp', context)

 

def get_delivery_charge_from_distance(lat1, long1, lat2, long2):
    """
    It takes 2 different lat, longs and return distance between them in km
    """
    distance = ceil(get_distance_between_two_locations(lat1, long1, lat2, long2))
    return 40 if distance <= 4 else distance * 10


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    return None if pdf.err else HttpResponse(result.getvalue(), content_type='application/pdf')


def get_razorpay_payment_id(captured_data):  # pragma: no cover
    """
    :params json captured_data: request body
    :returns: payment_id
    """
    return captured_data['payload']['payment']['entity']['id']


def get_user_order_data_from_razorpay_payload(captured_data):  # pragma: no cover
    """
    :params json captured_data: request body
    :returns: order_id, usr_id
    """
    razorpay_order_id = captured_data['payload']['payment']['entity']['order_id']
    user_id = captured_data['payload']['payment']['entity']['notes']['user_id']
    return razorpay_order_id, user_id
