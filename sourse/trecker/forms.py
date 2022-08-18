from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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


class UseradddelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk')
        super().__init__(*args, **kwargs)
        self.fields['users'].queryset = get_user_model().objects.exclude(pk=pk)


    class Meta:
        model = Project
        fields = ['users']
        widgets = {
            "users": widgets.CheckboxSelectMultiple
        }