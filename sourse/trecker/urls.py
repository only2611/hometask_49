from django.urls import path



from trecker.views import IndexView, TaskView, CreateView, Update, Delete

urlpatterns = [
    path('', IndexView.as_view(), name="index_view"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    path('create/', CreateView.as_view(), name="create"),
    path('task/<int:pk>/update', Update.as_view(), name="update"),
    path('task/<int:pk>/delete', Delete.as_view(), name="delete"),

]
