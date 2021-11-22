from django.db import models
from imagekit.models.fields import ImageSpecField
from pilkit.processors.resize import ResizeToFill

# Create your models here.

class SliderImage(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/utils/%Y/%m')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(1800,1119)])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
