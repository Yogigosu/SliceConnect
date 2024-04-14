from django.utils.text import slugify
 
from random import randint


def getStars(s):
    whole = int(s)
    ar = []
    for i in range(whole):
        ar.append('fa-star')
    if len(ar) == 5: return ar
    if (s - whole) == 0:
        for i in range(len(ar),5,1):
            ar.append('fa-star-o')
    else:
        ar.append('fa-star-half-o')
        for i in range(len(ar),5,1):
            ar.append('fa-star-o')
    return ar

def getReviewStatus(score):
    if score == 0.00: return 'n/a'
    if score >= 1.00 and score < 2.00:
        return 'Very Poor'
    elif score >= 2.00 and score < 3.00:
        return "Poor"
    elif score >= 3.00 and score < 4.00:
        return "Medium"
    elif score >= 4.00 and score < 4.50:
        return "Good"
    elif score >= 4.50 and score <= 5.00:
        return "Very Good"

def valid_phone(phone):
    if len(phone) != 11 or phone[0] != '0' or phone[1] != '1':
        return False
    if not re.compile("^[0-9]+$").match(phone):
        return False
    return True
def phone_already_exist(phone):
    from accounts.models import Account
    qs = Account.objects.filter(phone=phone)
    if qs.exists():
        return True
    return False

 

 

