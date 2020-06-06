from django import forms
from students.models import Student

class add_student_form(forms.ModelForm):
    """docstring for ."""

    class Meta:
        """docstring for ."""
        model = Student
        fields = ('image','fullname','email','phone')
