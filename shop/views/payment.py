from django.shortcuts import render, redirect
from shop.models import Product, User, Payment
from instamojo_wrapper import Instamojo
from download_projects.settings import PAYMENT_API_KEY, PAYMENT_API_AUTH_TOKEN

API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

import math


# Create your views here.
def createPayment(request, product_id):
    # Create a new Payment Request
    user = request.session.get('user')
    product = Product.objects.get(id=product_id)
    userObject = User.objects.get(id=user.get('id'))
    amount = (product.price - (product.price * (product.discount / 100)))
    response = API.payment_request_create(
        amount=math.floor(amount),
        purpose=f'Payment for {product.name}',
        send_email=True,
        buyer_name=userObject.name,
        email=user.get('email'),
        redirect_url="http://127.0.0.1:8000/complete-payment"
    )
    print(response)
    payment_request_id = response['payment_request']['id']
    # print the long URL of the payment request.
    payment = Payment(user=User(id = user.get('id') ) ,
                      product=product,
                      payment_request_id=payment_request_id)

    payment.save()

    url = response['payment_request']['longurl']
    print(response)
    return redirect(url)
    # print the unique ID(or payment request ID)
    # print response['payment_request']['id']

# Create your views here.
def verifyPayment(request):
    payment_id = request.GET.get('payment_id')
    payment_request_id = request.GET.get('payment_request_id')
    # Create a new Payment Request
    response = API.payment_request_payment_status(payment_request_id , payment_id)

    status = response['payment_request']['payment']['status']
    if status != 'Failed':
        payment =  Payment.objects.get(payment_request_id = payment_request_id)
        payment.payment_id = response['payment_request']['payment']['payment_id']
        payment.status = status
        payment.save()

        return render(request,"download_product_after_payment.html" , {'payment':payment})
    else:
        return render(request , "payment_fail.html" )

