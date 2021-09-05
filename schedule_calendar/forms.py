from django import forms
from schedule_calendar.models import Task


class TaskCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    start_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=True)
    end_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=True)

    class Meta:
        model = Task
        exclude = ('id',)
