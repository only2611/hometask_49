from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from trecker.forms import ProjectForm, FindForm, UseradddelForm
from trecker.models import Project

class ProjectsView(ListView):
    model = Project
    template_name = "projects/index.html"
    context_object_name = "projects"
    ordering = ("-start_date")
    paginate_by = 5


    def get(self, request, *args, **kwargs):
        self.form = self.get_find_form()
        self.search_value = self.get_find_value()
        return super().get(request, *args, **kwargs)


    def get_queryset(self):
        if self.search_value:
            return Project.objects.filter(Q(name__icontains=self.search_value)|
                                       (Q(description__icontains=self.search_value)))
        return Project.objects.all()


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



class AddUserView(UpdateView):
    form_class = UseradddelForm
    template_name = "projects/new_user.html"
    model = Project

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse("trecker:project-view", kwargs={"pk": self.object.pk})


class CreateProjectView(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = "projects/new-project.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse("trecker:project-view", kwargs={"pk": self.object.pk})


class ProjectView( DetailView):
    template_name = "projects/project.html"
    model = Project



class UpdateProject(LoginRequiredMixin, UpdateView):
    form_class = ProjectForm
    template_name = "projects/update_project.html"
    model = Project


    def get_success_url(self):
        return reverse("trecker:project-view", kwargs={"pk": self.object.pk})


class DeleteProject(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "projects/delete.html"
    success_url = reverse_lazy("trecker:p-view")