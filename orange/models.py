from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django import template
register = template.Library()
from django.contrib.auth import get_user_model
User= get_user_model()

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="eventowner",blank=True)
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True,blank=True)
    created_at= models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True,default='')
    description_short = models.TextField(blank=True,default='')
    additional_info = models.TextField(blank=True,default='')
    mainpic = models.ImageField(upload_to="orange/css/eventpics",height_field=None,width_field=None,max_length=1000,blank=True,null=True)
    price = models.TextField(blank=True,default='')
    link_to_external_site=models.TextField(blank=True,default='')
    link_button_text=models.TextField(blank=True,default='')
    org = models.ForeignKey('Organization',null=True,blank=True, on_delete=models.CASCADE)
    tendies = models.ManyToManyField(User,blank=True,related_name="tendies")

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug= slugify(self.name)

        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('orange:event',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-created_at']

class Day(models.Model):

    def day_default():
        return {
        "1":"free",
        "2":"free",
        "3":"free",
        "4":"free",
        "5":"free",
        "6":"free",
        "7":"free",
        "8":"free",
        "9":"free",
        "10":"free",
        "11":"free",
        "12":"free",
        "13":"free",
        "14":"free",
        "15":"free",
        "16":"free",
        "17":"free",
        "18":"free",
        "19":"free",
        "20":"free",
        "21":"free",
        "22":"free",
        "23":"free",
        "24":"free"}

    date= models.DateTimeField()
    events = models.ManyToManyField("Event",blank=True)
    closed = models.BooleanField(default=False)
    times = models.JSONField(encoder=None, decoder=None,default=day_default)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['date']

class Organization(models.Model):
    members = models.ManyToManyField(User,blank=True,related_name="org_member")
    admins = models.ManyToManyField(User,blank=True,related_name="org_admin")
    member_requests = models.ManyToManyField(User,blank=True,related_name="org_request")
    president = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE,related_name="org_president")
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True,blank=True)
    created_at= models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True,default='')
    mainpic = models.ImageField(upload_to="orange/css/clubpics",height_field=None,width_field=None,max_length=1000,blank=True,null=True)
    link_to_external_site=models.TextField(blank=True,default='')
    link_button_text=models.TextField(blank=True,default='')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug= slugify(self.name)

        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('orange:organization',kwargs={'slug':self.slug})
