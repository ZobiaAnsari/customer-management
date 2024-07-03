from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    user= models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name