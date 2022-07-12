from django.contrib import admin

# Register your models here.

from trecker.models import Task, Status, Type

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','summary', 'description', 'status',]
    list_display_links = ['summary']
    list_filter = ['status']
    search_fields = ['summary', 'status']
    fields = ['summary', 'description', 'status', 'types', 'created_at', 'updated_at',]
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Task, TaskAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name',]

admin.site.register(Status, StatusAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name',]


admin.site.register(Type, TypeAdmin)