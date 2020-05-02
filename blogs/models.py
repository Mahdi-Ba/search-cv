from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from datetime import datetime

# Create your models here.
from users.models import User


class Status(models.Model):
    title = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    en_title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    text = RichTextUploadingField(blank=True, null=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    sort = models.BigIntegerField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    en_title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    text = RichTextUploadingField(blank=True, null=True)
    sort = models.BigIntegerField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    en_title = models.CharField(max_length=255, null=True, blank=True,unique=True)
    text = RichTextUploadingField(blank=True, null=True)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    visit = models.BigIntegerField(null=True, blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    index = models.BooleanField(default=False)
    prev_article = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='prev_item')
    next_article = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_item')
    period = models.CharField(max_length=255, null=True, blank=True)
    image_alt = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from elasticsearch import Elasticsearch
# @receiver(post_save, sender=Article)
# def update_stock(sender, instance, **kwargs):
#     elastic_host = {"host": "localhost", "port": 9200}
#     es = Elasticsearch(hosts=[elastic_host])
# myBook = {
#     "author": "sina",
#     "price": "45.00",
#     "name": "DjangoForWebDevelopers",}
# es.index(index='books', doc_type='book', id=1, body=myBook)
# book_result_query = es.search(index='books',doc_type='book', body={'query': {'match': {'author': 'sina'}}})
# print(book_result_query)
#
#


class SearchLog(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title

