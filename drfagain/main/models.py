from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Animals(models.Model):
    title=models.CharField('title',max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    categ = models.ForeignKey('Category_Animals',on_delete=models.PROTECT,) #+= _id
    user = models.ForeignKey(User,verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Category_Animals(models.Model):
    name = models.CharField(max_length=150,db_index=True)


    def __str__(self):
        return self.name