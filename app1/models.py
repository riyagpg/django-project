from django.db import models

# Create your models here.
class Userregister(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField(default="")
    password=models.CharField(max_length=50)
    def __str__(self) -> str:
        return str(self.name)
    
class Category(models.Model):
    name=models.CharField(max_length=250,null=True)
    img=models.ImageField(upload_to="category_Img",null=True)
    def __str__(self) -> str:
        return str(self.name)

class Product(models.Model):
    categoryname=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    price=models.IntegerField(null=True)
    description=models.TextField(null=True)
    img=models.ImageField(upload_to="product_Img",null=True)
    quantity=models.IntegerField()
    #def __str__(self) -> str:
     #   return str(self.name)

class Order(models.Model):
    userid=models.CharField(max_length=250)
    productid=models.CharField(max_length=250)
    quantity=models.CharField(max_length=250)
    paymentamt=models.CharField(max_length=250,null=True)
    paymentmethod=models.CharField(max_length=250)
    transactionid=models.CharField(max_length=250)
    datetime=models.DateTimeField(auto_now=True,auto_created=True)


class Contactus(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    number=models.IntegerField(null=True)
    message=models.TextField()
    def __str__(self) -> str:
        return str(self.name)