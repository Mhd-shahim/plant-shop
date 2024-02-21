from django.db import models
from django.contrib.auth.models import User
from admin_dashboard.models import Plant
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    creared_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.plant.price * self.quantity
    
    def __str__(self):
        return str(self.user)+"-"+str(self.plant)
    
