from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from trecker.models import Type, Status, Task

FAVORITE_TYPES_CHOICES = [
    ('task', 'Task'),
    ('bug', 'Bug'),
    ('enhancement', 'Enhancement'),
]


# class TaskForm(forms.Form):
#     summary = forms.CharField(max_length=100, required=True, label='Имя')
#     description = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
#     status = forms.ModelChoiceField(queryset=Status.objects.all())
#     types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),
#                                            required=False,
#                                            label="ТИП ЗАДАЧИ",
#                                            widget=forms.CheckboxSelectMultiple,)


class TaskForm(forms.ModelForm):
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
