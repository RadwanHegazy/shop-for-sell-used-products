from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Profile (models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/user-images/',default='static/user-images/avatar.svg')
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=30,blank=True)
    products = models.ManyToManyField(Product,related_name='user_saved_products',blank=True)

    def __str__(self) :
        return f"{self.user}"

