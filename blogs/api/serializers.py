from django.utils.text import slugify
from rest_framework import serializers
from ..models import Article, Tag, Category
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



class CategorySerilizer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(source='en_title')

    class Meta:
        model = Category
        fields = '__all__'

    def get_slug(self, instance):
        return slugify(instance)


class TagSerilizer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(source='en_title')

    class Meta:
        model = Tag
        fields = '__all__'

    def get_slug(self, instance):
        return slugify(instance)


class BrifArticleSerilizer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(source='en_title')

    class Meta:
        model = Article
        fields = ['id', 'title', 'en_title', 'slug', 'period', 'image_alt', 'image']

    def get_slug(self, instance):
        return slugify(instance)


class ArticleSerilizer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(source='en_title')
    tag = TagSerilizer(many=True)
    next_article = BrifArticleSerilizer()
    prev_article = BrifArticleSerilizer()

    class Meta:
        model = Article
        fields = '__all__'

    def get_slug(self, instance):
        return slugify(instance)
