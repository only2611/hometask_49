from django.urls import reverse
from django.views.generic import CreateView, ListView

from trecker.forms import ProjectForm
from trecker.models import Project

class ProjectsView(ListView):
    model = Project
    template_name = "projects/index.html"
    context_object_name = "projects"
    ordering = ("start_date")
    paginate_by = 3


class CreateProjectView(CreateView):
    form_class = ProjectForm
    template_name = "projects/new-project.html"


    def get_success_url(self):
        return reverse("p-view")

