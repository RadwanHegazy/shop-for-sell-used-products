from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelStateFieldsCacheDescriptor
from products.models import Product
# Create your models here.
class Messages (models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    reciver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='client') 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='Product')
    msg = models.CharField(max_length=500,null=True)
    image = models.ImageField(upload_to='static/chat-images/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self) :
        return f"{self.sender} -> {self.reciver} ({self.product})"

class Ask (models.Model) :
    user = models.ForeignKey(User,related_name='userisAsk',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='useraskforthisproduct',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self) :
        return f"{self.user} -> {self.product}"