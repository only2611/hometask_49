from django.urls import path



from trecker.views import IndexView, TaskView, CreateView

urlpatterns = [
    path('', IndexView.as_view(), name="index_view"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    path('create/', CreateView.as_view(), name="create")

]

#     path('task/<int:pk>/update', update_note, name="update_note"),
#     path('task/<int:pk>/delete', delete, name="delete"),