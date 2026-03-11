from django.db import models
from django.utils import timezone 

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    message=models.CharField(max_length=100)
    address=models.TextField(default='')

    def __str__(self):
        return self.name

class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    password=models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    profile_pricture=models.ImageField(upload_to='profile_pricture',null=True, blank=True)
    usertype=models.CharField(max_length=100, default='buyer')


    def __str__(self):
        return self.fname+" "+self.lname
    
class Product1(models.Model):
    category = (
        ('all-colection', 'all-colection'),
        ('mobile', 'Mobile'),
        ('camera', 'Camera'),
        ('headphone', 'Headphone'),
        ('laptop', 'Laptop'),
        ('speakers', 'Speakers'),
    )

    seller=models.ForeignKey(User, on_delete=models.CASCADE)
    product_category=models.CharField(max_length=100,choices=category)
    product_name=models.CharField(max_length=100)
    product_price=models.PositiveIntegerField()
    product_desc=models.TextField()
    profile_pricture=models.ImageField(upload_to='profile_pricture')

    def __str__(self):
        return self.seller.fname+" - "+ self.product_name


class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product1,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.fname + " "+ self.product.product_name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product1,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    product_price=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()
    product_qut=models.PositiveIntegerField(default=1)
    payment_status=models.BooleanField(default=False)

 
    def __str__(self):
        return self.user.fname + " "+ self.product.product_name