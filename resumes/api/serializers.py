from django.utils.text import slugify
from rest_framework import serializers
from prerequisites.api.serializers import WorkingAreaSerilizer, OrganizationSizeSerilizer
from prerequisites.models import WorkingArea, OrganizationSize
from ..models import *


class ResumeDetailSerilizer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(source='owner')
    owner = serializers.CharField(read_only=True, source='owner.last_name')
    text = serializers.CharField(max_length=1024)
    info = serializers.JSONField(required=False,allow_null=False,)

    class Meta:
        model = Resume
        fields = ['id', 'slug', 'text', 'info','owner']

    def get_slug(self, instance):
        return slugify(instance.owner.first_name + "-" + instance.owner.last_name)



    def create(self, validate_data):
        resume = Resume.objects.create(**validate_data)
        return resume


    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.info = validated_data.get('info', instance.info)
        instance.save()
        return instance
