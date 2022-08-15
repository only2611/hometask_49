from django.contrib import admin

# Register your models here.

from trecker.models import Task, Status, Type, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','summary', 'description',]
    list_display_links = ['summary']
    list_filter = ['status']
    search_fields = ['summary', 'status']
    fields = ['summary', 'description', 'status', 'types', 'created_at', 'updated_at', 'User',]
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['types',]


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


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'start_date', 'finish_date',]
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name', 'description', 'start_date', 'finish_date', 'User',]
    filter_horizontal = ['users']

admin.site.register(Project, ProjectAdmin)