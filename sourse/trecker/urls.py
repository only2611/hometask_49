from django.urls import path



from trecker.views import IndexView, TaskView, CreateProjectView, ProjectsView, \
    CreateTaskView, ProjectView, UpdateTask, UpdateProject, DeleteTask, DeleteProject

urlpatterns = [
    path('tasks/', IndexView.as_view(), name="index_view"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    path('project/<int:pk>/createtask/', CreateTaskView.as_view(), name="create"),
    path('task/<int:pk>/update', UpdateTask.as_view(), name="update"),
    path('task/<int:pk>/delete', DeleteTask.as_view(), name="delete"),
    path('', ProjectsView.as_view(), name="p-view"),
    path('projects/add', CreateProjectView.as_view(), name="create-view"),
    path('projects/<int:pk>/view', ProjectView.as_view(), name="project-view"),
    path('project/<int:pk>/update', UpdateProject.as_view(), name="p-update"),
    path('project/<int:pk>/delete', DeleteProject.as_view(), name="p-delete"),

]
