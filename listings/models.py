from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    milage = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='main_images/')
    def __str__(self):
        return self.name

class Image(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')
    
    def __str__(self):
        return f"Image for {self.listing.name}"


