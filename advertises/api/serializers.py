from django.utils.text import slugify
from rest_framework import serializers
from companies.api.serializers import CompanySerilizer
from prerequisites.api.serializers import WorkingAreaSerilizer, OrganizationSizeSerilizer
from prerequisites.models import WorkingArea, OrganizationSize
from ..models import *


class AdvertiseDetailSerilizer(serializers.ModelSerializer):
    company = CompanySerilizer(many=False, read_only=True,required=False)
    slug = serializers.SerializerMethodField(source='owner')
    owner = serializers.CharField(read_only=True, source='owner.last_name')
    text = serializers.CharField(max_length=1024)
    title = serializers.CharField(max_length=300,required=False)
    en_title = serializers.CharField(max_length=300,required=False)
    info = serializers.JSONField(required=False, allow_null=False, )
    company_src = serializers.IntegerField(write_only=True, source='company',required=False,allow_null=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Advertise
        fields = ['id','title','en_title', 'slug', 'text', 'info', 'company', 'owner','company_src','status']

    def get_slug(self, instance):
        return slugify(instance.en_title)

    def validate_company_src(self, value):
        try:
            if value == -1:
                return value
            if Company.objects.filter(pk=value).exists():
                return value
            raise serializers.ValidationError("incorrect value Not any instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be integer")

    def create(self, validate_data):
        if validate_data.get('company', False):
            if Company.objects.filter(pk=validate_data['company'],owner=validate_data['owner']).exists():
                validate_data['company'] = Company.objects.get(pk=validate_data['company'])
            else:
                validate_data['company'] =None
        resume = Advertise.objects.create(**validate_data)
        return resume

    def update(self, instance, validated_data):
        if validated_data.get('company') and validated_data.get('company') != -1 :
            instance.company = Company.objects.get(pk=validated_data.get('company', instance.company))
        if validated_data.get('company') == -1:
            instance.company = None
        instance.text = validated_data.get('text', instance.text)
        instance.title = validated_data.get('title', instance.title)
        instance.en_title = validated_data.get('en_title', instance.en_title)
        instance.info = validated_data.get('info', instance.info)
        instance.save()
        return instance
