from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from django.utils.translation import ugettext_lazy as _
from accounts.models import Account

#----------------- SIGN UP VALIDATIONS -----------------
 
# Phone validation
def validatePhone(phone):
    # Length check
    if len(phone) != 11:
        raise ValidationError(
            _('Enter your 11 digit phone number'),
        )
    # 01xxxxxxxxx format check
    if phone[0] != '0' or phone[1] != '1':
        raise ValidationError(
            _("Consider this format: 01xxxxxxxxx")
        )
    # Numeric check
    if not re.compile("^[0-9]+$").match(phone):
        raise ValidationError(
            _('Invalid phone number.'),
        )
    # Already exists check
    qs = Account.objects.filter(phone=phone)
    if qs.exists():
        raise ValidationError(
            _("'%(phone)s' is already registered"), params={'phone':phone}
        )
 
# Name validation
def validateName(name):
    if not re.compile("^[A-Za-z .-]+$").match(name):
        raise ValidationError(
            _('"%(name)s" contains invalid character.'), params={'name': name},
        )
