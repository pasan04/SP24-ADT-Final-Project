from django.db import IntegrityError
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Avg
from project.models import Students,Teacher, Marks, CompositeKey
from django.contrib import messages
from django.db.models import Q
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend which doesn't require a GUI
import matplotlib.pyplot as plt
import io

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

def update_student(request, sid):
    student = Students.objects.get(sid=sid)
    student = Students.objects.get(sid=sid)
    return render(request, 'updateStudent.html', {'student':student})


def call_update_student_function(request, sid):
    student = Students.objects.get(sid=sid)

    name = request.POST['name']
    email = request.POST['email']
    age = request.POST['age']
    grade = request.POST['grade']

    student.name = name
    student.email = email
    student.age = age
    student.grade = grade

    student.save()
    messages.success(request, 'Data has been updated successfully!')
    return render(request, 'updateStudent.html', {'student': student})

def update_teacher(request, tid):
    teacher = Teacher.objects.get(tid=tid)
    return render(request, 'updateTeacher.html', {'teacher':teacher})

def call_update_teacher_function(request, tid):
    teacher = Teacher.objects.get(tid=tid)

    name = request.POST['name']
    email = request.POST['email']

    teacher.name = name
    teacher.email = email

    teacher.save()
    messages.success(request, 'Data has been updated successfully!')
    return render(request, 'updateTeacher.html', {'teacher': teacher})


def delete_student(request, id):
    Students.objects.filter(sid=id).delete()
    return redirect('/students')


def filter_students(request):
    # Get the single query parameter from the request
    query = request.GET.get('query', '')

    # Filter students based on the query parameter across name, email, and grade (case-insensitive)
    filtered_students = Students.objects.filter(
        Q(name__icontains=query) | Q(email__icontains=query) | Q(grade__icontains=query)
    )

    # Render the 'students.html' template with the filtered students
    return render(request, 'students.html', {'students': filtered_students})


def filter_teachers(request):
    # Get the single query parameter from the request
    query = request.GET.get('query', '')

    # Filter teachers based on the query parameter across name and email.
    filtered_teachers = Teacher.objects.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    )

    # Render the 'students.html' template with the filtered students
    return render(request, 'teachers.html', {'teachers': filtered_teachers})



def teachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': all_teachers})

def add_teacher(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Teacher.objects.create(name=name, email=email)
        messages.success(request, 'Data has been added successfully!')
    return render(request, 'addTeacher.html')

def delete_teacher(request, id):
    Teacher.objects.filter(tid=id).delete()
    return redirect('/teachers')

def marks(request):
    all_marks = Marks.objects.select_related('composite_key__sid').all()
    return render(request, 'marks.html', {'marks': all_marks})

def add_mark(request):
    all_students = Students.objects.all()

    if request.method == 'POST':
        # Get form data
        subject_id = request.POST.get('subject_id')
        sid = request.POST.get('sid')
        subject_name = request.POST.get('subject_name')
        marks = request.POST.get('marks')

        # Retrieve the Students instance using the provided sid
        student = get_object_or_404(Students, sid=sid)

        try:
            # Create the composite key
            composite_key, created = CompositeKey.objects.get_or_create(
                sid=student,
                subject_id=subject_id
            )

            if not created:
                # If composite key already exists, provide an error message
                messages.error(request, 'Composite key already exists.')
                return render(request, 'addMark.html', {'students': all_students})

            # Create a new Marks instance using the composite key
            Marks.objects.create(
                composite_key=composite_key,
                subject_name=subject_name,
                marks=marks
            )

            messages.success(request, 'Data has been added successfully!')
            return redirect('/marks/')

        except IntegrityError:
            # If an IntegrityError occurs, handle it and provide feedback
            messages.error(request, 'Integrity error: Composite key already exists.')
            return render(request, 'addMark.html', {'students': all_students})

    # Render the 'addMark.html' template if the request method is not POST
    return render(request, 'addMark.html', {'students': all_students})

def get_update_mark(request, subject_id, sid):
    all_students = Students.objects.all()

    composite_key = get_object_or_404(CompositeKey, subject_id=subject_id, sid=sid)

    # Retrieve the Marks instance using the composite key
    mark = get_object_or_404(Marks, composite_key=composite_key)

    context = {
        'students': all_students,
        'mark': mark,
        'subject_id': subject_id,
        'sid': sid
    }

    return render(request, 'updateMark.html', context)

def update_mark(request, subject_id, sid):
    # Retrieve the CompositeKey instance
    composite_key = get_object_or_404(CompositeKey, subject_id=subject_id, sid=sid)

    # Retrieve the Marks instance using the composite key
    mark = get_object_or_404(Marks, composite_key=composite_key)

    # If it's a POST request, handle form submission
    if request.method == 'POST':
        # Get form data
        subject_name = request.POST.get('subject_name')
        subject_id = request.POST.get('subject_id')
        marks_value = request.POST.get('marks')

        # Update the mark instance with new data
        mark.subject_name = subject_name
        mark.subject_id = subject_id
        mark.marks = marks_value

        # Save the updated instance
        mark.save()

        # Redirect to the marks list page or a success page
        return redirect('/marks/')

    # Prepare the context dictionary
    context = {
        'mark': mark
    }

    # Render the updateMark.html template with the context
    return render(request, 'updateMark.html', context)


def delete_mark(request, subject_id, sid):
    try:
        # Find the CompositeKey instance based on the provided subject_id and sid
        composite_key = CompositeKey.objects.get(subject_id=subject_id, sid=sid)
        # Find the corresponding Marks instance using the composite key
        mark_to_delete = Marks.objects.get(composite_key=composite_key)

        mark_to_delete.delete()

        return redirect('/marks')

    except (CompositeKey.DoesNotExist, Marks.DoesNotExist):
        # Handle the case where the CompositeKey or Marks instance does not exist
        # You may choose to log an error, show a custom error message, or simply redirect to the marks page
        return redirect('/marks')

def filter_marks(request):
    # Get the single query parameter from the request
    query = request.GET.get('query', '')

    # Filter marks based on the query parameter across subject name, subject ID, and marks (case-insensitive)
    filtered_marks = Marks.objects.filter(
        Q(subject_name__icontains=query) | Q(composite_key__subject_id__icontains=query) | Q(marks__icontains=query)
    )

    # Render the 'marks.html' template with the filtered marks
    return render(request, 'marks.html', {'marks': filtered_marks})



def plot_marks_bar_graph(request):
    # Aggregate marks data from the database
    marks_data = Marks.objects.values('subject_name').annotate(avg_marks=Avg('marks'))

    # Extract subjects and average marks from aggregated data
    subjects = [item['subject_name'] for item in marks_data]
    avg_marks = [item['avg_marks'] for item in marks_data]

    # Embed the graph data into the HTML template context
    context = {
        'subjects': subjects,
        'marks': avg_marks
    }

    # Render the template with the context
    return render(request, 'marks_graph.html', context)



