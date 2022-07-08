from django.urls import path

from trecker.views import index_view

urlpatterns = [
    path("", index_view, name="index_view"),


]


# path("create/", create, name="create"),
#     path('task/<int:pk>/update', update_note, name="update_note"),
#     path('task/<int:pk>/delete', delete, name="delete"),