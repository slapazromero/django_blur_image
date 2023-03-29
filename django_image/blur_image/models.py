from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
import os

# Create your models here.
class Image(models.Model):
    name_image = models.CharField('Name Image', max_length = 15)
    image = models.ImageField('Image', blank=True, null=True, upload_to = 'media')
    is_blur = models.BooleanField('Is Blur?', default = False)
    
    def __unicode__(self,):
        return str(self.image)
    
@receiver(pre_delete, sender=Image)
def _image_delete(sender, instance, using, **kwargs):
    file_path = settings.MEDIA_ROOT + str(instance.image)
    print(file_path)
    if os.path.isfile(file_path):
        os.remove(file_path)