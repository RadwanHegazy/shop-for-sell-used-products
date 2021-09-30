from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from products.models import Product
# Create your views here.

@login_required
def profile (request) :
    products = Product.objects.filter(user=request.user)
    return render(request,'profile/profile.html',{'products':products})

def view_profile (request,username) :
    user = get_object_or_404(User,username=username)
    if request.user == user :
        return redirect('profile')
    return render(request,'profile/view_user.html',{'view':user})


@login_required
def edit_profile (request) :
    if request.POST or request.FILES : 
        if 'image' in request.FILES : 
            image = request.FILES['image']
            prof = Profile.objects.get(user=request.user)
            prof.image = image
            prof.save()
        
        if 'username' in request.POST: 
            username = request.POST['username']
            email = request.POST['email']
            usr = User.objects.get(username=request.user.username)
            usr.username = username
            usr.email = email
            usr.save()

        if 'phone' in request.POST:
            phone = request.POST['phone']
            ph = Profile.objects.get(user=request.user)
            ph.phone = phone
            ph.save()

        return redirect('edit_profile')
    return render(request,'profile/edit_profile.html')