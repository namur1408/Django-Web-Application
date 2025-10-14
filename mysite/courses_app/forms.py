from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'start_date', 'end_date', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple()
        }
