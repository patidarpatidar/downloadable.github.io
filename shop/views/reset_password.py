from django.views import View
from django.shortcuts import render ,redirect ,HttpResponse
from django.contrib.auth.hashers import check_password
from shop.models import User
from shop.utils.email_sender import sendEmail
class ResetPassword(View):
    def get(self, request):
        return render(request , 'reset_password.html')

    def post(self, request):
        pass;
        # email = request.POST.get('email')
        # print(email)
        # return HttpResponse(email)
import math
import random
class PasswordResetVerification(View):
    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.object.get(email=email)
            print(user)
            otp = math.floor(random.random() * 10000000)
            html = f'''
                    <h4> Your Password reset Verification Code is {otp}</h4>
                    '''
            sendEmail("user",
                      email,
                      "Password Reset Verification Code", html)
            request.session['reset-password-verification-code'] = otp
            request.session['reset-password-email'] = email
            return HttpResponse("email sent")
        except:
            return redirect('/reset-password')