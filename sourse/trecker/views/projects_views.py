from django.db.models import Q
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from trecker.forms import ProjectForm, FindForm
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

class CreateProjectView(CreateView):
    form_class = ProjectForm
    template_name = "projects/new-project.html"


    def get_success_url(self):
        return reverse("p-view")


class ProjectView(DetailView):
    template_name = "projects/project.html"
    model = Project



class UpdateProject(UpdateView):
    form_class = ProjectForm
    template_name = "projects/update_project.html"
    model = Project


    def get_success_url(self):
        return reverse("project-view", kwargs={"pk": self.object.pk})


