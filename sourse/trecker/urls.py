from django.urls import path



from trecker.views import IndexView, TaskView

urlpatterns = [
    path('', IndexView.as_view(), name="index_view"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),

]


# path("create/", create, name="create"),
#     path('task/<int:pk>/update', update_note, name="update_note"),
#     path('task/<int:pk>/delete', delete, name="delete"),