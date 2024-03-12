from django.shortcuts import render,redirect
from django.http import HttpResponse
from project.models import Students
from django.contrib import messages

#reffered - Create crud application with Django 3, Bootstrap 4 and SQLite - Part 1

def students(request):
    all_students = Students.objects.all()
    return render(request, 'students.html', {'students': all_students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        grade = request.POST['grade']
        Students.objects.create(name=name, email=email, age=age, grade=grade)
        messages.success(request, 'Data has been added successfully!')
    return render(request, 'addStudent.html')

def update_student(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        grade = request.POST['grade']
        Students.objects.get(sid=id).update(name=name, email=email, age=age, grade=grade)
        messages.success(request, 'Data has been updated successfully!')
    student = Students.objects.get(sid=id)
    return render(request, 'updateStudent.html', {'student':student})

def delete_student(request, id):
    Students.objects.filter(sid=id).delete()
    return redirect('/students')



