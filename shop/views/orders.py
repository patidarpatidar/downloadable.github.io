from django.shortcuts import render ,redirect
from shop.models import Product ,User , Payment

from django.db.models import Q

# Create your views here.
def my_orders(request):
    user_id = request.session.get('user').get('id')
    user = User(id = user_id)
    payments = Payment.objects.filter(~Q(status="Failed") , user = user)
    return render(request, 'orders.html' , {'orders' : payments});


