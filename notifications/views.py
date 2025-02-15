from django.shortcuts import render, HttpResponseRedirect
from .models import Notification
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def notificationList_view(request):
	template_name = 'notifications.html'
	account = Account.objects.get(user=request.user)
	notf_list = Notification.objects.all().filter(account=account)
	page = request.GET.get('page', 1)
	paginator = Paginator(notf_list, 10)
	try:
	    notifications = paginator.page(page)
	except PageNotAnInteger:
	    notifications = paginator.page(1)
	except EmptyPage:
	    notifications = paginator.page(paginator.num_pages)

	return render(request, template_name, {'notifications':notifications})

 