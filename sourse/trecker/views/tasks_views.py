from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode

from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from trecker.forms import TaskForm, FindForm
from trecker.models import Task, Project


class IndexView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = ("-updated_at")
    paginate_by = 5


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


    # def form_valid(self, form):
    #     task = get_object_or_404(Task, pk=self.kwargs.get("pk"))
    #     form.instance.task = task
    #     return super().form_valid(form)


    def get_success_url(self):
        return reverse("index_view")


class Update(View):
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = TaskForm(initial={
                "summary": self.task.summary,
                "description": self.task.description,
                "status": self.task.status,
                "types": self.task.types.all(),
                "project": self.task.project
            })
            return render(request, "tasks/update.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            self.task.summary = form.cleaned_data.get("summary")
            self.task.description = form.cleaned_data.get("description")
            self.task.status = form.cleaned_data.get("status")
            self.task.types.set(form.cleaned_data.get("types"))
            self.task.project = form.cleaned_data.get("project")
            self.task.save()
            return redirect("index_view", )
        return render(request, "tasks/update.html", {"form": form})



class Delete(View):
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, "tasks/delete.html", {"task": self.task})
    def post(self, request, *args, **kwargs):
            self.task.delete()
            return redirect("index_view")
