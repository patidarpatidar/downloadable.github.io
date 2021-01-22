from django.views import View
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from shop.models import User

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            hashedPassword = make_password(password = password)
            user = User(name=name, email=email, password=hashedPassword, phone=phone)
            user.save()
            return render(request , 'login.html')
        except:
            return render(request , 'signup.html' , {'error':"User already register "})
