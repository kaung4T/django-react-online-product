from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True, blank=True)
    user2 = models.ManyToManyField(User, default=None, related_name='user2_list', null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    
