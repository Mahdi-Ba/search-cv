from django.contrib import admin

# Register your models here.
from resumes.models import Status, Resume
from django_json_widget.widgets import JSONEditorWidget
from jsonfield import JSONField


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']



@admin.register(Resume)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ['user', 'owner', 'status','created_at','updated_at']
    search_fields = ['user', 'owner']
    readonly_fields = ['user']
    list_filter = ['status']
    ordering = ('-created_at',)
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

