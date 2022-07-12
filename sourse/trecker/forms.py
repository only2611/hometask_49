from django import forms

from trecker.models import Type, Status

FAVORITE_TYPES_CHOICES = [
    ('task', 'Task'),
    ('bug', 'Bug'),
    ('enhancement', 'Enhancement'),
]


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='Имя')
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),
                                           required=False,
                                           label="ТИП ЗАДАЧИ",
                                           widget=forms.CheckboxSelectMultiple,)
