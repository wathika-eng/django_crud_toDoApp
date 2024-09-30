from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "image", "due_date", "alarm_time"] 
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter note title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your note here", "rows": 5}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "due_date": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "alarm_time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
        }
