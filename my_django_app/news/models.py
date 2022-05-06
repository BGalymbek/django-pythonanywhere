from datetime import date 
from distutils.command.upload import upload
import email
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Articles(models.Model):
    title=models.CharField('Тағам аты',max_length=50)
    anons=models.CharField('Сипаттамасы',max_length=250)
    full_text=models.TextField('Толық сипаттама')
    date = models.DateTimeField('Жариялаған күні')
    video=models.FileField('Upload Video',upload_to="main/img/", null=True, blank=True)
    imgs= models.ImageField('Upload image',upload_to="main/img/", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    """ @property
    def imageURL(self):
        try:
            url = self.imgs.url
        except:
            url = ''
        return url  """   
    
    class Meta:
        verbose_name='Тағам'
        verbose_name_plural='Тағамдар'

class Quram(models.Model):
    name=models.CharField('Аты',max_length=50)
    qurams=models.TextField('Құрам')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Құрамы'
        verbose_name_plural='Құрамдар'

class Qundylyq(models.Model):
    food_title=models.CharField('Тағам',max_length=50)
    aquz=models.CharField('Ақуыз',max_length=50)
    mai=models.CharField('Май',max_length=50)
    ksutek=models.CharField('Көмірсутек',max_length=50)

    def __str__(self):
        return self.food_title
    
    class Meta:
        verbose_name='Құндылық'
        verbose_name_plural='Құндылықтары'

class Post(models.Model):
    title=models.CharField(max_length=255,verbose_name='Тақырып')
    is_published=models.BooleanField(default='True', verbose_name='Шығармашылық')
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
        ordering=['title']

class Logs(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    age=models.CharField(max_length=100)

    def __str__(self):
        return self.username



