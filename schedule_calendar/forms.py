from django import forms


class EventCreateForm(forms.ModelForm):

    start_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=True)
    end_date = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"], required=False)

    #def set_calendar(self, calendar_id):
    #    event = self.instance
    #    event.calendar_id = calendar_id
    #    self.instance = event

    class Meta:
        model = Event
        exclude = ('calendar',)
