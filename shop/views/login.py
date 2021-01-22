from django.views import View
from django.shortcuts import render ,redirect
from django.contrib.auth.hashers import check_password
from shop.models import User

class LoginView(View):
    def get(self, request):

        return_url = None
        print('from class based view')
        LoginView.return_url = request.GET.get('return_url')

        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            flag = check_password(password=password, encoded=user.password)
            if flag:
                #hiding navbar ke liye  user se email or id ko hold kiya
                temp = {}
                temp['email'] = user.email
                temp['id'] = user.id
                request.session['user'] = temp
                # end hiding navbar ke liye  user se email or id ko hold kiya

                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                return redirect('index')

            else:
                return render(request, 'login.html', {'error': "Email or Password Invalid"})
        except:
            return render(request, 'login.html', {'error': "Email or Password Invalid"})
