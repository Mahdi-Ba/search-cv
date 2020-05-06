from django.utils.text import slugify
from rest_framework import serializers
from prerequisites.api.serializers import WorkingAreaSerilizer, OrganizationSizeSerilizer
from prerequisites.models import WorkingArea, OrganizationSize
from ..models import *


class CompanySerilizer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=False, allow_null=False, required=True)

    # user = serializers.CharField(required=False)

    class Meta:
        model = Company
        fields = ['id', 'title', ]
        # exclude = ('title', )

    def validate_title(self, value):
        try:
            if not Company.objects.filter(title=value).exists():
                return value
            raise serializers.ValidationError("incorrect value instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be string")


class CompanyDetailSerilizer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(source='en_title')
    parent = CompanySerilizer(many=False, read_only=True)
    working_area = WorkingAreaSerilizer(read_only=True, many=True)
    size = OrganizationSizeSerilizer(many=False, read_only=True)
    owner = serializers.CharField(read_only=True, source='user.last_name')
    title = serializers.CharField(required=False)
    address = serializers.CharField(allow_null=True,required=False)
    phone = serializers.CharField(allow_null=True,required=False)
    en_title = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    description = serializers.CharField()
    working_area_Company = serializers.PrimaryKeyRelatedField(many=True, write_only=True, required=False, source='working_area', queryset=WorkingArea.objects.all())
    company_size = serializers.IntegerField(write_only=True, source='size', required=False)
    parent_Company = serializers.IntegerField(write_only=True, source='parent', required=False)
    image_alt = serializers.ReadOnlyField()
    keywords = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    index = serializers.ReadOnlyField()
    sort = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['id', 'owner', 'size', 'working_area', 'title', 'en_title', 'image', 'image_alt', 'text', 'keywords',
                  'description', 'status', 'created_at', 'updated_at', 'index', 'sort', 'parent', 'slug',
                  'working_area_Company', 'company_size', 'parent_Company','address','phone'
                  ]

    def get_slug(self, instance):
        return slugify(instance)

    def validate_company_size(self, value):
        try:
            if OrganizationSize.objects.filter(pk=value).exists():
                return value
            raise serializers.ValidationError("incorrect value Not any instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be integer")

    def validate_parent_Company(self, value):
        try:
            if Company.objects.filter(pk=value).exists():
                return value
            raise serializers.ValidationError("incorrect value Not any instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be integer")

    def validate_title(self, value):
        try:
            if not Company.objects.filter(title=value).exists():
                return value
            raise serializers.ValidationError("incorrect value Duplicate")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be str")

    def validate_en_title(self, value):
        try:
            if not Company.objects.filter(en_title=value).exists():
                return value
            raise serializers.ValidationError("incorrect value Duplicate")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be str")

    def create(self, validate_data):
        if validate_data.get('size', False):
          validate_data['size'] = OrganizationSize.objects.get(pk=validate_data['size'])
        if validate_data.get('parent',False):
             validate_data['parent'] = Company.objects.get(pk=validate_data['parent'])
        working_area = validate_data.pop('working_area', False)
        company = Company.objects.create(**validate_data)
        if working_area:
            company.working_area.set(working_area)
        return company

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.en_title = validated_data.get('en_title', instance.en_title)
        if validated_data.get('parent'):
          instance.parent = Company.objects.get(pk=validated_data.get('parent', instance.parent))
        if validated_data.get('size'):
             instance.size = OrganizationSize.objects.get(pk=validated_data.get('size', instance.size))
        if validated_data.get('working_area'):
            instance.working_area.set(validated_data.get('working_area', instance.working_area))
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
