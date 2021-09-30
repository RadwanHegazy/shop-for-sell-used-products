from typing import Counter
from chat.models import Messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from products.models import Product
from .models import Messages, Ask
from django.db.models import Q
# Create your views here.


def owner_chat (request,product_name,consumer_name) :
    product = get_object_or_404(Product,name=product_name)
    consumer = get_object_or_404(User,username=consumer_name)
    owner = request.user
    
    context = {'product':product,
                'consumer':consumer}

    return render(request,'chat/owner_chat_side.html',context)


def index (request,product_name) :

    if request.user.is_authenticated :
        product = get_object_or_404(Product,name=product_name)

        if request.user == product.user :
            return redirect('home')
        
        context = {
            'product':product
        }
        return render(request,'chat/index.html',context)
    else :
        return redirect('login')


def send_msg (request,id) :
    pro = get_object_or_404(Product,id=id)
    
    if 'image' in request.FILES :
        image = request.FILES['image']
        Messages.objects.create(sender=request.user,reciver=pro.user,product=pro,image=image)
    
    
    # send msg as client
    msg = request.POST['msg']

    if msg != "":
        Messages.objects.create(msg=msg,sender=request.user,reciver=pro.user,product=pro).save()
        Ask.objects.get_or_create(user=request.user,product=pro)

    
    return JsonResponse(data='Done',safe=False)


def owner_msg (request) :

    # fetch data
    user = request.user
    consumer_id = request.POST['consumer_id']
    product_id = request.POST['product_id']
    msg = request.POST['msg']


    # get info from db
    consumer = User.objects.get(id=consumer_id)
    product = Product.objects.get(id=product_id)

    if 'image' in request.FILES :
        image = request.FILES['image']
        Messages.objects.create(sender=user,reciver=consumer,product=product,image=image)
    
    # create the message
    if msg != "":
        Messages.objects.create(sender=user,reciver=consumer,product=product,msg=msg)
    else :
        pass

    return JsonResponse(data="Message is sent", safe=False)




def view_chats_for_products (request) :
    if request.user.is_authenticated == False :
        return redirect('login')
    products = Product.objects.filter(user=request.user).order_by('date')

    get_msgs = Messages.objects.filter(Q(reciver=request.user)).order_by('date')
    
    get_msgs.update(seen=True)

    data = []
    

    if 'product-name' in request.GET :
        p_name = request.GET['product-name']
        if p_name == 'all' :
            for i in products :
                all_msgs = Ask.objects.filter(product=i)
                for c in all_msgs :
                    data.append({
                        'client':c.user,
                        'product':c.product,
                        'date':c.date
                    })

        else :
            p_query = Product.objects.get(user=request.user,name=p_name)
            ask_data = Ask.objects.filter(product=p_query)
            for i in ask_data :
                data.append({
                    'client':i.user,
                    'product':i.product,
                    'date':i.date
                })

    else :
    
        for i in products :
            all_msgs = Ask.objects.filter(product=i)
            for c in all_msgs :
                data.append({
                    'client':c.user,
                    'product':c.product,
                    'date':c.date
                })

    
    

    
    return render(request,'chat/prduct_chats.html',{'ps':products,'data':data})


def view_all_msgs (request,pro):
    product = get_object_or_404(Product,name=pro)
    get_msgs = Messages.objects.filter(Q(reciver=request.user,product=product)|Q(sender=request.user,product=product)).order_by('date')
    return JsonResponse(data=list(get_msgs.values_list('sender','reciver','msg','image')),safe=False)

def del_asker (request, user_id) :
    get_user = get_object_or_404(User,id=user_id)
    Ask.objects.get(user=get_user).delete()

    return redirect('viewchats')


def view_unseen_msgs(request) :
    user = request.user
    if user.is_authenticated :
        get_msgs = Messages.objects.filter(reciver=user).all().exclude(seen=True)
        return JsonResponse(data=get_msgs.count(),safe=False)
    else :
        return JsonResponse(data="Not Loged in",safe=False)