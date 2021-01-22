from django.shortcuts import render ,redirect
from shop.models import Product



# Create your views here.
def index(request):

    products = Product.objects.filter(active=True)
    data = {
        'products': products
    }

    return render(request, 'index.html', data);

def logout(request):
    request.session.clear()
    return redirect('index')

