from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from jsonfield import JSONField

from companies.models import Company
from users.models import User

class Status(models.Model):
    title = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.title

class Advertise(models.Model):
    title = models.CharField(blank=False,null=False,max_length=300,default=None)
    en_title = models.CharField(blank=False,null=False,max_length=300,default=None)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='useradvertize')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,blank=True, null=True,)
    text = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    info = JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.owner.first_name