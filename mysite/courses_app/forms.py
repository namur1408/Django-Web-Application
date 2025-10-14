from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter course name', 'class': "form-control"}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter course description', 'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }
