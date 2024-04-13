from django import forms
from .models import Assignment,Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'instructor_name', 'description', 'semester']
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['course_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['instructor_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['description'].widget.attrs.update({'class': 'form-control'})
            self.fields['semester'].widget.attrs.update({'class': 'form-control'})

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'assignment_name', 'due_date', 'description']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['course'].widget.attrs.update({'class': 'form-control'})
            self.fields['assignment_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['due_date'].widget.attrs.update({'class': 'form-control'})
            self.fields['description'].widget.attrs.update({'class': 'form-control','rows' : '1'})

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class': 'form-control'})
            self.fields['email'].widget.attrs.update({'class': 'form-control'})
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})

