from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from prerequisites.models import Status, OrganizationSize, WorkingArea
from users.models import User


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='owner')
    size = models.ForeignKey(OrganizationSize, on_delete=models.SET_NULL, null=True, blank=True)
    working_area = models.ManyToManyField(WorkingArea, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    en_title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    image = models.ImageField(upload_to='company/', null=True, blank=True)
    image_alt = models.CharField(max_length=255, null=True, blank=True)
    text = RichTextUploadingField(blank=True, null=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    index = models.BooleanField(default=False)
    sort = models.BigIntegerField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
