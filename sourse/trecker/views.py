

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from trecker.models import Task


def index_view(request):
    notes = Task.objects.all()
    notes = notes.order_by("-created_at")
    context = {"notes": notes}
    return render(request, "index.html", context, )
