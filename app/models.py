from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
import os
from uuid import uuid4

# Create your models here.

class Profile(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   institute = models.CharField(max_length=256, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

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

choice = (('Libro','Libro'),('Revista','Revista'),('Meme','Meme'),('Publicidad', 'Publicidad'))
   
class Corpus(models.Model):
    gender_choice = ('Libro','Revista','Meme','Publicidad')
    corpus_name = models.CharField(max_length=100,null=True,blank=True)
    recollection_country = models.CharField(max_length=4,null=True,blank=True)
    corpus_description = models.CharField(max_length=500,null=True,blank=True)
    start_date_publication = models.DateField(null=True,blank=True)
    final_date_publication = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=40, null=True,blank=True, choices = choice)
    approved = models.BooleanField(null=True,blank=True, default=False)
    corpus_document = models.FileField(null=True,blank=True)
    corpus_pdf = models.FileField(null=True,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    uploaded_date= models.DateField(auto_now_add=True, null=True, blank = True)
    updated_date= models.DateField(auto_now_add=True, null= True, blank=True)

class Segmentation(TimeStampMixin):
    image=models.ImageField(upload_to=path_and_rename)
    document_name=models.CharField(max_length=200)
    code=models.CharField(max_length=500)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True, default = request.user)
    start=models.CharField(max_length=100,null=True,blank=True)
    end=models.CharField(max_length=100,null=True,blank=True)
    weight=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    area_size = models.DecimalField(max_digits=50,decimal_places=2,null=True,blank=True)
    selected = models.BooleanField(null=True,blank=True, default=False)
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE, null=True, blank=True)

    
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

