from django.db import models

from blur_image.utils import image_upload_location

# Create your models here.
class Image(models.Model):
    name_image = models.CharField('Name Image', max_length = 15)
    image = models.ImageField('Image', blank=True, null=True, upload_to = 'images')
    is_blur = models.BooleanField('Is Blur?', default = False)