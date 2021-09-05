from django import forms
from django.core.exceptions import ValidationError

from schedule_calendar.models import Task

class TaskCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    start_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=True)
    end_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=True)

    class Meta:
        model = Task
        exclude = ('id',)

    def clean(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        if start_date <= end_date:
            raise forms.ValidationError("Erro ao criar tarefa. A data de início deve ser menor que a data do fim de uma tarefa.")

        return self.cleaned_data

class TaskEditForm(forms.ModelForm):
    task_id = forms.IntegerField()
    name = forms.CharField(max_length=100, required=True)
    start_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=True)
    end_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=False)

    def save(self, commit=True):
        task = Task.objects.get(id=self.cleaned_data["task_id"])
        task.name = self.cleaned_data["name"]
        task.start_date = self.cleaned_data["start_date"]
        task.end_date = self.cleaned_data["end_date"]
        if commit:
            task.save()

        return task

    def clean(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        if start_date <= end_date:
            raise forms.ValidationError("Erro ao criar tarefa. A data de início deve ser menor que a data do fim de uma tarefa.")

        return self.cleaned_data


    class Meta:
        model = Task
        exclude = ("id",)
