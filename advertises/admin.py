from django.contrib import admin
from elasticsearch import Elasticsearch
from .models import Status, advertise
from django_json_widget.widgets import JSONEditorWidget
from jsonfield import JSONField


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['user', 'owner', 'company', 'status', 'created_at', 'updated_at']
    search_fields = ['user', 'owner']
    readonly_fields = ['user']
    list_filter = ['status']
    ordering = ('-created_at',)
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    autocomplete_fields = ['company']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        elastic_data = obj.info
        if obj.status != None:
            elastic_data["status"] = {"id": obj.status.id, "title": obj.status.title}
        elastic_host = {"host": "localhost", "port": 9200}
        es = Elasticsearch(hosts=[elastic_host])
        es.index(index='advertises', doc_type='advertise', id=obj.id, body=elastic_data)
        # book_result_query = es.search(index='books', doc_type='book', body={'query': {'match': {'author': 'sina'}}})

    def delete_model(self, request, obj):
        elastic_host = {"host": "localhost", "port": 9200}
        es = Elasticsearch(hosts=[elastic_host])
        es.delete(index='advertises', doc_type='advertise', id=obj.id)
        super().delete_model(request, obj)
