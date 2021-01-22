from django.views import View
from django.shortcuts import HttpResponse
import random
import math

from shop.utils.email_sender import sendEmail


def sendOtp(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    otp = math.floor(random.random() * 10000000)
    html = f'''
                 <h4>hello {name} </h4>
                 <br>
                 <p>your Verification Code is</p> <b>{otp}</b>
                 <br>
                 <p>if you didnt requested verfication code , you can ignore this email</p>
            '''
    print(name, email)
    if name and email:
        response = sendEmail(name=name, email=email, htmlContent=html, subject='verify Email')

        try:
            if (response.status_code == 200):
                request.session['verification-code'] = otp
                return HttpResponse("{'message':'success'}", status=200)
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)


def verifyCode(request):
    code = request.POST.get('code')

    otp = request.session.get('verification-code')

    if (str(otp) == code):
        return HttpResponse("{'message':'success'}", status=200)
    else:
        return HttpResponse(status=400)
