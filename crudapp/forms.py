from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'image', 'is_completed', 'due_date', 'alarm_time'] 
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'alarm_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
