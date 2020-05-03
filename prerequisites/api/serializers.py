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


class OrganizationSizeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationSize
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

class AbilityDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'


class AbilitySerilizer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=False, allow_null=False,required=True)
    # user = serializers.CharField(required=False)

    class Meta:
        model = Ability
        fields = ['id','title',]
        # exclude = ('title', )

    def validate_title(self, value):
        try:
            if not Ability.objects.filter(title=value).exists():
                return value
            raise serializers.ValidationError("incorrect value instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be string")





class MajorDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class MajorSerilizer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=False, allow_null=False,required=True)
    # user = serializers.CharField(required=False)

    class Meta:
        model = Major
        fields = ['id','title',]
        # exclude = ('title', )

    def validate_title(self, value):
        try:
            if not Major.objects.filter(title=value).exists():
                return value
            raise serializers.ValidationError("incorrect value instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be string")




class UniversityDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UniversitySerilizer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=False, allow_null=False,required=True)
    # user = serializers.CharField(required=False)

    class Meta:
        model = University
        fields = ['id','title',]
        # exclude = ('title', )

    def validate_title(self, value):
        try:
            if not University.objects.filter(title=value).exists():
                return value
            raise serializers.ValidationError("incorrect value instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be string")



class WorkingAreaDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = WorkingArea
        fields = '__all__'


class WorkingAreaSerilizer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=False, allow_null=False,required=True)
    # user = serializers.CharField(required=False)

    class Meta:
        model = WorkingArea
        fields = ['id','title',]
        # exclude = ('title', )

    def validate_title(self, value):
        try:
            if not WorkingArea.objects.filter(title=value).exists():
                return value
            raise serializers.ValidationError("incorrect value instance found")
        except ValueError:
            raise serializers.ValidationError("incorrect value should be string")