import django_filters
from .models import Student
from django import forms

class StudentFilter(django_filters.FilterSet):
	class Meta:
		model = Student
		fields = ['student_name', 'father_name', 'select_program']
		labels = {
		'student_name' : '',
		'father_name' : '',
		'select_program' : '',
		}
		widgets = {
            'student_name': forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'father_name': forms.TextInput(attrs={'placeholder': 'Father Name'}),
        }