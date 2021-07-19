from django.shortcuts import render, redirect
from .models import Products


# Create your views here.
def index(request):
    return render(request, 'index.html')


def select(request):
    products = Products.objects.all()
    # print("this is the products object", products)
    return render(request, 'select.html', {'products': products})


def Insert(request):
    if request.method == 'POST':
        print('request came!!!!!!!!@@@@@@@@@@@@@@@@@@@@@@@@@')
        request_data = request.POST;
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        if (name is None) or (description is None) or (price is None):
            print('something was none')
        else:
            product = Products(name=name, description=description, price=price)
            print('new product was created!!!')
            product.save()
        return redirect('/select')

    return render(request, 'home.html')


def edit(request, id):
    products = Products.objects.get(id=id)
    #form = Products(instance=products)

    # needs to be changed!!!!!!
    if request.method == 'POST':
        form = Products()
        return redirect('/select')
    return render(request, 'edit.html')


def delete(request, id):
    products = Products.objects.get(id=id)
    products.delete()
    return redirect('/select')

def search(request):
    search = request.GET['search']
    products = Products.objects.filter(name__icontains=search)
    params = {'products': products}
    return render(request, 'search.html', params)
