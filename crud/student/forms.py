from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		labels = {
		'student_name' : '',
		'father_name' : '',
		'phone_no' : '',
		'select_program' : '',
		}
		widgets = {
            'student_name': forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'father_name': forms.TextInput(attrs={'placeholder': 'Father Name'}),
            'phone_no': forms.TextInput(attrs={'placeholder': 'Phone No'}),
        }