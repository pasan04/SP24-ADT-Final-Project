from django.db import models

# Create your models here.
class Students(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    grade = models.IntegerField()
    class Meta:
        db_table = "students"


class CompositeKey(models.Model):
    sid = models.OneToOneField(Students, on_delete=models.CASCADE)
    subject_id = models.CharField(max_length=20)

    class Meta:
        # Define composite primary key
        unique_together = ('sid', 'subject_id')

class Marks(models.Model):
    composite_key = models.OneToOneField(CompositeKey, primary_key=True, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=255)
    marks = models.IntegerField()


class Teacher(models.Model):
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.name

class TeacherStudent(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'student')



