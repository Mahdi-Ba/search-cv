from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from ..models import *
from django.db.models import Q
from drf_yasg.utils import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


class GenderList(APIView):
    @swagger_auto_schema(
        operation_description="get GenderList",
        responses={200: GenderSerilizer(many=True)}
    )
    def get(self, request, format=None):
        gender = Gender.objects.all()
        gender_serlizer = GenderSerilizer(gender, many=True)
        return Response(gender_serlizer.data)


class SizeList(APIView):
    @swagger_auto_schema(
        operation_description="get SizeList",
        responses={200: OrganizationSizeSerilizer(many=True)}
    )
    def get(self, request, format=None):
        orgsize = OrganizationSize.objects.all()
        orgsize_serlizer = OrganizationSizeSerilizer(orgsize, many=True)
        return Response(orgsize_serlizer.data)


class LanguageSkillList(APIView):
    @swagger_auto_schema(
        operation_description="get LanguageSkillSerilizer",
        responses={200: LanguageSkillSerilizer(many=True)}
    )
    def get(self, request, format=None):
        language_skill = LanguageSkill.objects.all()
        language_skill_serlizer = LanguageSkillSerilizer(language_skill, many=True)
        return Response(language_skill_serlizer.data)


class LanguageList(APIView):
    @swagger_auto_schema(
        operation_description="get LanguageSerilizer",
        responses={200: LanguageSerilizer(many=True)}
    )
    def get(self, request, format=None):
        language = Language.objects.all()
        language_serlizer = LanguageSerilizer(language, many=True)
        return Response(language_serlizer.data)

    @swagger_auto_schema(
        responses={200: LanguageSerilizer(many=True)}

    )
    def post(self, request, format=None):
        language = Language.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()
        language_serlizer = LanguageSerilizer(language, many=True)
        return Response(language_serlizer.data)


class ProvincelList(APIView):
    @swagger_auto_schema(
        operation_description="get ProvinceSerilizer",
        responses={200: ProvinceSerilizer(many=True)}
    )
    def get(self, request, format=None):
        province = Province.objects.all()
        province_serlizer = ProvinceSerilizer(province, many=True)
        return Response(province_serlizer.data)

    @swagger_auto_schema(
        responses={200: ProvinceSerilizer(many=True)}

    )
    def post(self, request, format=None):
        province = Province.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()
        province_serlizer = ProvinceSerilizer(province, many=True)
        return Response(province_serlizer.data)


class CitylList(APIView):
    @swagger_auto_schema(
        operation_description="get CitySerilizer",
        responses={200: CitySerilizer(many=True)}
    )
    def get(self, request, pk, format=None):
        city = City.objects.filter(province=pk).all()
        city_serlizer = CitySerilizer(city, many=True)
        return Response(city_serlizer.data)

    @swagger_auto_schema(
        responses={200: CitySerilizer(many=True)}

    )
    def post(self, request, pk, format=None):
        city = City.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item']), province=pk).all()
        city_serlizer = CitySerilizer(city, many=True)
        return Response(city_serlizer.data)


class BenefitlList(APIView):
    @swagger_auto_schema(
        operation_description="get BenefitsJobSerilizer",
        responses={200: BenefitsJobSerilizer(many=True)}
    )
    def get(self, request, format=None):
        benefit = BenefitsJob.objects.all()
        benefit_serlizer = BenefitsJobSerilizer(benefit, many=True)
        return Response(benefit_serlizer.data)


class MilitaryList(APIView):
    @swagger_auto_schema(
        operation_description="get MilitarySerilizer",
        responses={200: MilitarySerilizer(many=True)}
    )
    def get(self, request, format=None):
        milatry = Military.objects.all()
        milatry_serlizer = MilitarySerilizer(milatry, many=True)
        return Response(milatry_serlizer.data)


class MaritalStatusList(APIView):
    @swagger_auto_schema(
        operation_description="get MaritalStatusSerilizer",
        responses={200: MaritalStatusSerilizer(many=True)}
    )
    def get(self, request, format=None):
        marital = MaritalStatus.objects.all()
        marital_serlizer = MaritalStatusSerilizer(marital, many=True)
        return Response(marital_serlizer.data)


class JobSkillList(APIView):
    @swagger_auto_schema(
        operation_description="get SkillLevelSerilizer",
        responses={200: SkillLevelSerilizer(many=True)}
    )
    def get(self, request, format=None):
        skill = SkillLevel.objects.all()
        skill_serlizer = SkillLevelSerilizer(skill, many=True)
        return Response(skill_serlizer.data)


class GradeList(APIView):
    @swagger_auto_schema(
        operation_description="get GradeSerilizer",
        responses={200: GradeSerilizer(many=True)}
    )
    def get(self, request, format=None):
        grade = Grade.objects.all()
        grade_serlizer = GradeSerilizer(grade, many=True)
        return Response(grade_serlizer.data)


class SocialMediaList(APIView):
    @swagger_auto_schema(
        operation_description="get SocialMediaSerilizer",
        responses={200: SocialMediaSerilizer(many=True)}
    )
    def get(self, request, format=None):
        socila = SocialMedia.objects.all()
        socila_serlizer = SocialMediaSerilizer(socila, many=True)
        return Response(socila_serlizer.data)


class JobTimeList(APIView):
    @swagger_auto_schema(
        operation_description="get JobTimeSerilizer",
        responses={200: JobTimeSerilizer(many=True)}
    )
    def get(self, request, format=None):
        job_time = JobTime.objects.all()
        job_time_serlizer = JobTimeSerilizer(job_time, many=True)
        return Response(job_time_serlizer.data)


class AbilityStore(APIView):
    @swagger_auto_schema(
        request_body=AbilitySerilizer,
        responses={200: AbilitySerilizer(many=False)}
    )
    def post(self, request, format=None):
        ability = AbilitySerilizer(data=request.data)
        if ability.is_valid():
            ability.save(user=request.user)
            return Response(ability.data, status=status.HTTP_200_OK)
        return Response(ability.errors, status=status.HTTP_400_BAD_REQUEST)


class AbilityList(APIView):
    @swagger_auto_schema(
        operation_description="get ability_serlizer",
        responses={200: AbilitySerilizer(many=True)}
    )
    def post(self, request, format=None):
        ability = Ability.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()[:14]
        ability_serlizer = AbilitySerilizer(ability, many=True)
        return Response(ability_serlizer.data)

    @swagger_auto_schema(
        operation_description="get AbilityDetailSerilizer",
        responses={200: AbilityDetailSerilizer(many=False)}
    )
    def get(self, request, pk, format=None):
        ability = Ability.objects.get(pk=pk)
        ability_serlizer = AbilityDetailSerilizer(ability, many=False)
        return Response(ability_serlizer.data)


class MajorStore(APIView):
    @swagger_auto_schema(
        request_body=MajorSerilizer,
        responses={200: MajorSerilizer(many=False)}
    )
    def post(self, request, format=None):
        major = MajorSerilizer(data=request.data)
        if major.is_valid():
            major.save(user=request.user)
            return Response(major.data, status=status.HTTP_200_OK)
        return Response(major.errors, status=status.HTTP_400_BAD_REQUEST)


class MajorList(APIView):
    @swagger_auto_schema(
        operation_description="get MajorList",
        responses={200: MajorSerilizer(many=True)}
    )
    def post(self, request, format=None):
        major = Major.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()[:14]
        major_serlizer = MajorSerilizer(major, many=True)
        return Response(major_serlizer.data)

    @swagger_auto_schema(
        operation_description="get MajorList",
        responses={200: MajorDetailSerilizer(many=False)}
    )
    def get(self, request, pk, format=None):
        major = Major.objects.get(pk=pk)
        major_serlizer = MajorDetailSerilizer(major, many=False)
        return Response(major_serlizer.data)


class UniversityStore(APIView):
    @swagger_auto_schema(
        request_body=UniversitySerilizer,
        responses={200: UniversitySerilizer(many=False)}
    )
    def post(self, request, format=None):
        university = UniversitySerilizer(data=request.data)
        if university.is_valid():
            university.save(user=request.user)
            return Response(university.data, status=status.HTTP_200_OK)
        return Response(university.errors, status=status.HTTP_400_BAD_REQUEST)


class UniversityList(APIView):
    @swagger_auto_schema(
        responses={200: UniversitySerilizer(many=True)}
    )
    def post(self, request, format=None):
        university = University.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()[:14]
        university_serlizer = UniversitySerilizer(university, many=True)
        return Response(university_serlizer.data)

    @swagger_auto_schema(
        responses={200: UniversityDetailSerilizer(many=True)}
    )
    def get(self, request, pk, format=None):
        university = University.objects.get(pk=pk)
        university_serlizer = UniversityDetailSerilizer(university, many=False)
        return Response(university_serlizer.data)


class WorkingAreaStore(APIView):
    @swagger_auto_schema(
        request_body=WorkingAreaSerilizer,
        responses={200: WorkingAreaSerilizer(many=False)}
    )
    def post(self, request, format=None):
        workingarea = WorkingAreaSerilizer(data=request.data)
        if workingarea.is_valid():
            workingarea.save(user=request.user)
            return Response(workingarea.data, status=status.HTTP_200_OK)
        return Response(workingarea.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkingAreaList(APIView):
    @swagger_auto_schema(responses={200: WorkingAreaSerilizer(many=True)})
    def post(self, request, format=None):
        workingarea = WorkingArea.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()[:14]
        workingarea_serlizer = WorkingAreaSerilizer(workingarea, many=True)
        return Response(workingarea_serlizer.data)

    @swagger_auto_schema(responses={200: WorkingAreaDetailSerilizer(many=False)})
    def get(self, request, pk, format=None):
        workingarea = WorkingArea.objects.get(pk=pk)
        workingarea_serlizer = WorkingAreaDetailSerilizer(workingarea, many=False)
        return Response(workingarea_serlizer.data)


class JobPositionStore(APIView):
    @swagger_auto_schema(
        request_body=JobPositionSerilizer,
        responses={200: JobPositionSerilizer(many=False)}
    )
    def post(self, request, format=None):
        job_position = JobPositionSerilizer(data=request.data)
        if job_position.is_valid():
            job_position.save(user=request.user)
            return Response(job_position.data, status=status.HTTP_200_OK)
        return Response(job_position.errors, status=status.HTTP_400_BAD_REQUEST)


class JobPositionList(APIView):
    @swagger_auto_schema(responses={200: JobPositionSerilizer(many=True)})
    def post(self, request, format=None):
        job_position = JobPosition.objects.filter(
            Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()[:14]
        job_position_serlizer = JobPositionSerilizer(job_position, many=True)
        return Response(job_position_serlizer.data)

    @swagger_auto_schema(responses={200: JobPositionDetailSerilizer(many=False)})
    def get(self, request, pk, format=None):
        job_position = JobPosition.objects.get(pk=pk)
        job_position_serlizer = JobPositionDetailSerilizer(job_position, many=False)
        return Response(job_position_serlizer.data)

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
