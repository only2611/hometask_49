from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from trecker.models import Type, Status, Task, Project

FAVORITE_TYPES_CHOICES = [
    ('task', 'Task'),
    ('bug', 'Bug'),
    ('enhancement', 'Enhancement'),
]





class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["summary", "description", "status", "types"]
        widgets = {
            "types": widgets.CheckboxSelectMultiple
        }

class TaskForm2(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "types": widgets.CheckboxSelectMultiple
            }

    # def clean(self):
    #     if self.cleaned_data.get("summary") == self.cleaned_data.get("description"):
    #         raise ValidationError("Заголовок и описание не могут иметь одинаковые значения")
    #     return super().clean()


class FindForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'finish_date']