from django.db import models

# Create your models here.

class Student(models.Model):
	PROGRAM = (
		('BCS', 'BCS'),
		('FSC', 'FSC'),
		('BSC', 'BSC'),
		)
	student_name = models.CharField(max_length=120, null=True)
	father_name = models.CharField(max_length=120, null=True)
	phone_no = models.CharField(max_length=120, null=True)
	select_program = models.CharField(max_length=30, choices=PROGRAM)

	def __str__(self):
		return self.student_name