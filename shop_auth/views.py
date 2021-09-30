from django.shortcuts import redirect, render
from django.contrib.auth.views import auth_login
from .forms import SignupForm
from user_profile.models import Profile
# Create your views here.


def signup (request) :
    form = SignupForm()
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid() :
            user = form.save()
            auth_login(request,user=user)
            Profile.objects.create(user=request.user).save()
            return redirect('home')
    return render(request,'auth/signup.html',{'form':form})