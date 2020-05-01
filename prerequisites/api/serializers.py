from django.utils.text import slugify
from rest_framework import serializers
from ..models import *
from django.urls import reverse


class GenderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class LanguageSkillSerilizer(serializers.ModelSerializer):
    class Meta:
        model = LanguageSkill
        fields = '__all__'


class LanguageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ProvinceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class CitySerilizer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class BenefitsJobSerilizer(serializers.ModelSerializer):
    class Meta:
        model = BenefitsJob
        fields = '__all__'


class MilitarySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Military
        fields = '__all__'


class MaritalStatusSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'


class SkillLevelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SkillLevel
        fields = '__all__'


class GradeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class SocialMediaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class JobTimeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = JobTime
        fields = '__all__'
