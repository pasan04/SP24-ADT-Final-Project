from django.urls import path
from . import views

# URL Config module
urlpatterns = [
    path("", views.students, name = "students"),
    path("students/", views.students, name="students"),
    path('students/add/', views.add_student, name = 'addStudent'),
    path('students/update/<int:sid>/', views.update_student, name='updateStudent'),
    path('students/delete/<int:id>/', views.delete_student, name='deleteStudent'),
    path('students/filter/', views.filter_students, name='filter_students'),

    path('teachers/', views.teachers, name='teachers'),
    path('teachers/add/', views.add_teacher, name='addTeacher'),
    path('teachers/update/<int:tid>/', views.update_teacher, name='updateTeacher'),
    path('teachers/delete/<int:id>', views.delete_teacher, name='deleteTeacher'),

    path('marks/', views.marks, name='marks'),
    path('marks/add/', views.add_mark, name='addMark'),
    path('marks/update/<str:subject_id>/<int:sid>/', views.update_mark, name='updateMark'),
    path('marks/delete/<str:subject_id>/<int:sid>/', views.delete_mark, name='deleteMark'),
]


