from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import StudentFilter
from django.db.models import Q

# Create your views here.

@login_required(login_url='login')
def home(request):
	all_student = Student.objects.all()
	myFilter = StudentFilter(request.POST, queryset=all_student)
	all_student = myFilter.qs
	total_student = all_student.count()
	bcs_student = all_student.filter(select_program='BCS').count()
	fsc_student = all_student.filter(select_program='FSC').count()
	bsc_student = all_student.filter(select_program='BSC').count()
	context = {'myFilter' :myFilter ,'all_student' : all_student, 'bcs_student' : bcs_student, 
				'fsc_student'  : fsc_student, 'bsc_student' : bsc_student, 'total_student' : total_student}
	return render(request, 'student/index.html', context)


@login_required(login_url='login')
def add_student(request):
	student_form = StudentForm()
	if request.method == 'POST':
		student_form = StudentForm(request.POST)
		if student_form.is_valid():
			student_form.save()
			messages.info(request, 'User Added Successfully')
			return redirect("home")
		else:
			student_form = StudentForm()
	context = {'student_form' : student_form}
	return render(request, 'student/add_student.html', context)


@login_required(login_url='login')
def update_student(request, pk_test):
	select_student = Student.objects.get(id=pk_test)
	student_form = StudentForm(instance=select_student)
	if request.method == 'POST':
		form = StudentForm(request.POST, instance=select_student)
		if form.is_valid():
			form.save()
			messages.warning(request, 'Student Updated Successfully')
			return redirect('home')
		else:
			return HttpResponse("something Wrong")
	context = {'student_form' : student_form, 'select_student' : select_student}
	return render(request, 'student/add_student.html', context)


@login_required(login_url='login')
def delete_student(request, pk_test):
	select_student = Student.objects.get(id=pk_test)
	select_student.delete()
	messages.warning(request, 'Student Has Been Deleted Successfully')
	return redirect('home')


def sign_in(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Username OR Password is Incorrect")
	return render(request, 'student/sign-in.html')


def search_student(request):
	student = StudentForm(request.POST)
	context = {'student' : student}
	if request.method == 'POST':
		student = request.POST['student_name']
		father = request.POST['father_name']
		if student:
			match = Student.objects.filter(Q(student_name__icontains=student) & Q(father_name__icontains=father))
			total_match = Student.objects.filter(Q(student_name__icontains=student)).count()
			if match:
				return render(request, 'student/search.html', {'match' : match, 'total_match' : total_match})
			else:
				messages.error(request, "No Result Found")
	return render(request, 'student/search.html', context)


def logout_user(request):
	logout(request)
	return redirect('sign_in')





