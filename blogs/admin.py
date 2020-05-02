from django.contrib import admin
from .models import Status, Category, Tag, Article, SearchLog


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'user', 'parent', 'sort', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    autocomplete_fields = ['parent']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'user', 'sort', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'en_title', 'user', 'category', 'status', 'updated_at']
    search_fields = ['title', 'en_title']
    readonly_fields = ['user']
    list_filter = ['status', 'index']
    autocomplete_fields = ['category', 'prev_article', 'next_article', 'tag']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'user']
    search_fields = ['user']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request,obj=None):
        return False

    def has_delete_permission(self, request,obj=None):
        return False



