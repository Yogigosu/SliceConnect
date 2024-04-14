from accounts.models import Account
#from notifications.models import Notification


def account_processor(request):
	try:
		ACCOUNT = Account.objects.get(user=request.user)
	except:
		ACCOUNT = None
	return {'ACCOUNT': ACCOUNT}

 