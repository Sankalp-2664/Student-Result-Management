from django.db import models

# Create your models here.

# Student Model
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)  # Roll number as primary key
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=10)  # Class/Grade of the student

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.class_name}"

# Admin Model
class Admin(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.username

# Subject Model
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)  # Auto-incrementing ID for subjects
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

# Marks Model
class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)  # Auto-incrementing ID for marks
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ForeignKey to Student
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # ForeignKey to Subject
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks}"
