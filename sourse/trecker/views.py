


from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic import TemplateView

from trecker.models import Task

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Task.objects.all()
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

