from django.db import models
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
import os

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=100)
    description  = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    
class Plant(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length = 255, default=None)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    


#delete the associated image while the instance is deleted
    
@receiver(post_delete, sender=Banner)
def delete_banner_image(sender, instance, **kwargs):
    
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=Category)
def delete_category_image(sender, instance, **kwargs):
    
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=Plant)
def delete_plant_image(sender, instance, **kwargs):
    
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


#delete old image while the image field of an instance is changed
            
@receiver(pre_save, sender=Banner)
def delete_old_banner_image(sender, instance, **kwargs):
    if instance.pk: 
        old_banner = Banner.objects.get(pk=instance.pk)
        if old_banner.image != instance.image: 
            old_image_path = old_banner.image.path
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

@receiver(pre_save, sender=Category)
def delete_old_category_image(sender, instance, **kwargs):
    if instance.pk: 
        old_category = Category.objects.get(pk=instance.pk)
        if old_category.image != instance.image: 
            old_image_path = old_category.image.path
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

@receiver(pre_save, sender=Plant)
def delete_old_plant_image(sender, instance, **kwargs):
    if instance.pk: 
        old_plant = Plant.objects.get(pk=instance.pk)
        if old_plant.image != instance.image: 
            old_image_path = old_plant.image.path
            if os.path.exists(old_image_path):
                os.remove(old_image_path)