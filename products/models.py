from django.core.exceptions import RequestAborted
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelStateFieldsCacheDescriptor
# Create your models here.


class Product (models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userProduct',null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=1000)
    specs = models.TextField(max_length=5000,null=True)
    image = models.ImageField(upload_to='static/products-images/')
    date = models.DateTimeField(auto_now_add=True)


    def add_product (user,name,price,desc,specs,image) :
        pro = Product.objects.create(user=user,name=name,price=price,desc=desc,specs=specs,image=image)
        pro.save()

    def getAll () :
        return Product.objects.all().order_by('-date')

    def __str__ (self) :
        return f"{self.name}"

