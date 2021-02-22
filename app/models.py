from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from PIL import Image
import os
from uuid import uuid4

# Create your models here.

def path_and_rename(instance, filename):
    upload_to ="upload_images/"
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Segmentation(TimeStampMixin):
    image=models.ImageField(upload_to=path_and_rename)
    document_name=models.CharField(max_length=200)
    code=models.CharField(max_length=500)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    start=models.CharField(max_length=100,null=True,blank=True)
    end=models.CharField(max_length=100,null=True,blank=True)
    weight=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    area_size = models.DecimalField(max_digits=50,decimal_places=2,null=True,blank=True)
    selected = models.BooleanField(null=True,blank=True, default=False)

    def __str__(self):
        return self.document_name
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.path)
    def get_original_image_path(self):
        return self.image.url.split("/media/")[-1]

    def imageSize(self):
        im = Image.open(self.image.path)
        width, height = im.size
        print(width, height)
        return {width,height}

    def areaSize(self):
        print("Path",self.image.path)
        return os.path.getsize(self.image.path)