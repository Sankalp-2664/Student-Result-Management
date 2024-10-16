from django.db import models

# Create your models here.

# Student Model
class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=10)  # Reflects the 'class_name' field in SQL

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.class_name}"

# Admin Model
class Admins(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=128)  # For hashed passwords

    def __str__(self):
        return self.username

# Subject Model
class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

# Marks Model
class Marks(models.Model):
    mark_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)  # References Students table
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)  # References Subjects table
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks}"
    
class Course(models.Model):
    course_name = models.CharField(max_length=50, primary_key=True)

