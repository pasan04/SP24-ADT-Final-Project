# Generated by Django 5.0.3 on 2024-04-09 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositeKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=20)),
                ('sid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.students')),
            ],
            options={
                'unique_together': {('sid', 'subject_id')},
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('composite_key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='project.compositekey')),
                ('subject_name', models.CharField(max_length=255)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.students')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.teacher')),
            ],
            options={
                'unique_together': {('teacher', 'student')},
            },
        ),
    ]
