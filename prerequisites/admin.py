from django.contrib import admin

# Register your models here.
from prerequisites.models import Status, Ability, Province, City, Grade, Major


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'user', 'sort', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)



@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'user', 'sort', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title','province', 'user', 'sort', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status']
    autocomplete_fields = ['province']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'user', 'sort', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)



@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'user', 'sort', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

