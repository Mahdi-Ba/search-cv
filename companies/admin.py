from django.contrib import admin

# Register your models here.
from companies.models import Company, Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']



# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ['title', 'en_title', 'owner', 'size', 'sort', 'status', 'user', 'updated_at']
#     search_fields = ['title', 'en_title']
#     readonly_fields = ['user','owner']
#     list_filter = ['status']
#     autocomplete_fields = ['working_area']
#
#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         super().save_model(request, obj, form, change)
