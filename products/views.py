from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from . import models
from user_profile.models import Profile
import products
# Create your views here.



def home (request) :
    if 'search' in request.GET : 
        word = request.GET['search']
        products = models.Product.objects.filter(name__icontains=word)
    else :    
        products = models.Product.getAll()
    return render(request,'home/index.html',{'products':products})

def view_product (request, number):
    get = get_object_or_404(models.Product,id=number)
    return render(request,'home/view.html',{'product':get})

def add_product (request) :
    if request.method == 'POST':
        if 'image' in request.FILES :
            image = request.FILES['image']
        name = request.POST['prooductName']
        description = request.POST['prooductDesc']
        specs = request.POST.getlist('specs')
        user = request.user
        price = request.POST['price']
        for i in specs : data = str(i).replace(',',';')
        models.Product.add_product(user=user,name=name,desc=description,specs=data,image=image,price=price)

    return render(request,'products/add.html')


def del_product (request,pk) :
    product = get_object_or_404(models.Product,pk=pk)
    product.delete()
    return redirect('home')

def edit_product (request, pk) :
    product = get_object_or_404(models.Product,pk=pk)
    if request.method == 'POST' :

        price = request.POST['price']
        try :
            price = str(price).replace('$',"")
        except :
            pass
        name = request.POST['name']
        desc = request.POST['desc']
        specs = request.POST.getlist('specs')
        
        product.price = price
        product.name = name
        product.desc = desc

        for i in specs : data = str(i).replace(',',';')
        print(data)
        product.specs = data

        if 'image' in request.FILES :
            image = request.FILES['image']
            product.image = image

        product.save()



    if request.user != product.user :
        return redirect('home')
    else : 
        return render(request,'products/edit.html',{'product':product})

def save_prod (request,id) :
    user = request.user
    product = get_object_or_404(models.Product,id=id)

    get = Profile.objects.get(user=user)
    if product in get.products.all() :
        get.products.remove(product)
    else :
        get.products.add(product)
    return redirect('vpro',id)
 
def view_saved (request) :
    return render(request,'products/saved.html')