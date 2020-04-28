from django.contrib import admin

# Register your models here.
from companies.models import Company


@admin.register(Company)
class WorkingAreaAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'owner', 'size', 'sort', 'status', 'user', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status']
    autocomplete_fields = ['working_area']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
