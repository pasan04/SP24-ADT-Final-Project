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



