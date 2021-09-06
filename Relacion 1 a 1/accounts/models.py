from django.db import models
from django.contrib.auth.models import User



class costumer(models.Model):
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table = 'costumer'





class tag(models.Model):
    name = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'tag'        

class product(models.Model):
    CATEGORY = (('Indoor','Indoor'), ('Out door', 'Out door'))
    name = models.CharField(max_length=100,null=True)
    price = models.FloatField(max_length=100, null=True, )
    category= models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=100, null=True,blank=True)
    data_created = models.DateField(auto_now_add=True)
    tags=models.ManyToManyField(tag)

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'product'

class order(models.Model):
    STATUS= (('Pending', 'Pending'),
            ('Out for Delivery', 'Out for Delivery'),
            ('Delivered', 'Delivered'))


    costumer= models.ForeignKey(costumer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100, null=True, choices=STATUS)
    tags=models.ManyToManyField(tag)


    class Meta:
        db_table = 'order'
