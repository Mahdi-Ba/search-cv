from django.utils.text import slugify
from rest_framework import serializers
from ..models import Article, Tag
from django.urls import reverse


# class PageSerializer(serializers.ModelSerializer):
#     url = serializers.SerializerMethodField('get_url')
#
#     class Meta:
#         model = Page
#         fields = ['id', 'title', 'url']
#
#     def get_url(self, instance):
# #         return reverse('page_detail', kwargs={'slug': instance.slug})
#
# class TagSer(serializers.ModelSerializer):
#     # tag = serializers.StringRelatedField(many=True)
#     slug = serializers.SlugField(source='en_title')
#     class Meta:
#         model = Tag
#         fields = '__all__'
#
#
#
