from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode


from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from trecker.forms import TaskForm, FindForm, TaskForm2
from trecker.models import Task, Project


class IndexView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = ("-updated_at")
    paginate_by = 7


    def get(self, request, *args, **kwargs):
        self.form = self.get_find_form()
        self.search_value = self.get_find_value()
        return super().get(request, *args, **kwargs)


    def get_queryset(self):
        if self.search_value:
            return Task.objects.filter(Q(summary__icontains=self.search_value)|
                                       (Q(description__icontains=self.search_value)))
        return Task.objects.all()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            context['query'] = query
            context['search'] = self.search_value
        return(context)


    def get_find_form(self):
        return FindForm(self.request.GET)


    def get_find_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class TaskView(TemplateView):
    template_name = "tasks/task.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        kwargs["task"] = task
        return super().get_context_data(**kwargs)


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"


    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
       return reverse("trecker:project-view", kwargs={"pk": self.object.project.pk})


class CreateTaskView2(CreateView):
    model = Task
    form_class = TaskForm2
    template_name = "tasks/create.html"

    def get_success_url(self):
       # return reverse("project-view", kwargs={"pk": self.object.project.pk})
        return reverse("trecker:index_view")


class UpdateTask(UpdateView):
    form_class = TaskForm
    template_name = "tasks/update.html"
    model = Task


    def get_success_url(self):
        return reverse("trecker:task_view", kwargs={"pk": self.object.pk})



class DeleteTask(DeleteView):
    model = Task
    template_name = "tasks/delete.html"

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("trecker:project-view", kwargs={"pk": self.object.project.pk})





