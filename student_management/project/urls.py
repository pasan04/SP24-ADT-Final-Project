from django.urls import path
from . import views

# URL Config module
urlpatterns = [
    path("", views.students, name = "students"),
    path('add/', views.add_student, name = 'addStudent'),
    path('update/<int:id>/', views.update_student, name='updateStudent'),
    path('delete/<int:id>/', views.delete_student, name='deleteStudent'),
]


