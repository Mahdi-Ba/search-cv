from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from ..models import *


class GenderList(APIView):
    def get(self, request, format=None):
        gender = Gender.objects.all()
        gender_serlizer = GenderSerilizer(gender, many=True)
        return Response(gender_serlizer.data)


class LanguageSkillList(APIView):
    def get(self, request, format=None):
        language_skill = LanguageSkill.objects.all()
        language_skill_serlizer = LanguageSkillSerilizer(language_skill, many=True)
        return Response(language_skill_serlizer.data)


class LanguageList(APIView):
    def get(self, request, format=None):
        language = Language.objects.all()
        language_serlizer = LanguageSerilizer(language, many=True)
        return Response(language_serlizer.data)


class ProvincelList(APIView):
    def get(self, request, format=None):
        province = Province.objects.all()
        province_serlizer = ProvinceSerilizer(province, many=True)
        return Response(province_serlizer.data)


class CitylList(APIView):
    def get(self, request, pk, format=None):
        city = City.objects.filter(province=pk).all()
        city_serlizer = CitySerilizer(city, many=True)
        return Response(city_serlizer.data)


class BenefitlList(APIView):
    def get(self, request, format=None):
        benefit = BenefitsJob.objects.all()
        benefit_serlizer = BenefitsJobSerilizer(benefit, many=True)
        return Response(benefit_serlizer.data)


class MilitaryList(APIView):
    def get(self, request, format=None):
        milatry = Military.objects.all()
        milatry_serlizer = MilitarySerilizer(milatry, many=True)
        return Response(milatry_serlizer.data)


class MaritalStatusList(APIView):
    def get(self, request, format=None):
        marital = MaritalStatus.objects.all()
        marital_serlizer = MaritalStatusSerilizer(marital, many=True)
        return Response(marital_serlizer.data)


class JobSkillList(APIView):
    def get(self, request, format=None):
        skill = SkillLevel.objects.all()
        skill_serlizer = SkillLevelSerilizer(skill, many=True)
        return Response(skill_serlizer.data)


class GradeList(APIView):
    def get(self, request, format=None):
        grade = Grade.objects.all()
        grade_serlizer = GradeSerilizer(grade, many=True)
        return Response(grade_serlizer.data)


class SocialMediaList(APIView):
    def get(self, request, format=None):
        socila = SocialMedia.objects.all()
        socila_serlizer = SocialMediaSerilizer(socila, many=True)
        return Response(socila_serlizer.data)

# class CategoriesDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk,slug, format=None):
#         category = self.get_object(pk)
#         serializer = CategorySerilizer(category)
#         return Response(serializer.data)
