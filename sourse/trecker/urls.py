from django.urls import path



from trecker.views import IndexView, TaskView, Update, Delete, CreateProjectView, ProjectsView, \
    CreateTaskView, ProjectView

urlpatterns = [
    path('', IndexView.as_view(), name="index_view"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    path('create/', CreateTaskView.as_view(), name="create"),
    path('task/<int:pk>/update', Update.as_view(), name="update"),
    path('task/<int:pk>/delete', Delete.as_view(), name="delete"),
    path('projects/', ProjectsView.as_view(), name="p-view"),
    path('projects/add', CreateProjectView.as_view(), name="create-view"),
    path('projects/<int:pk>/view', ProjectView.as_view(), name="project-view"),

]
