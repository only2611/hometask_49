


from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic import TemplateView

from trecker.forms import TaskForm
from trecker.models import Task

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


# class IndexView(View):
#     def get(self,request):
#         notes = Task.objects.all()
#         context = {"notes": notes}
#         return render(request, "index.html", context, )

class TaskView(TemplateView):
    template_name = "task.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        kwargs["task"] = task
        return super().get_context_data(**kwargs)



class CreateView(View):
    def get(self, request, **kwargs):
        if request.method == "GET":
            form = TaskForm()
            return render(request, "create.html", {"form": form})
    def post(self, request):
            form = TaskForm(data=request.POST)
            if form.is_valid():
                summary = form.cleaned_data.get("summary")
                description = form.cleaned_data.get("description")
                status = form.cleaned_data.get("status")
                type = form.cleaned_data.get("type")
                new_task = Task.objects.create(summary=summary, description=description, status=status, type=type)
                return redirect("index_view", )
            return render(request, "create.html", {"form": form})


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
                "type": self.task.type,
            })
            return render(request, "update.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            self.task.summary = form.cleaned_data.get("summary")
            self.task.description = form.cleaned_data.get("description")
            self.task.status = form.cleaned_data.get("status")
            self.task.type = form.cleaned_data.get("type")
            self.task.save()
            return redirect("index_view", )
        return render(request, "update.html", {"form": form})


# def delete(request, pk):
#     note = get_object_or_404(Task, pk=pk)
#     if request.method == "GET":
#         return render(request, "delete.html", {"note": note})
#     else:
#         note.delete()
#         return redirect("index_view")
