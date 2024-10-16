from django.shortcuts import get_object_or_404, render
from .models import Students, Marks

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def student_list(request):
    students = Students.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_marks(request, student_id):
    # Fetch the student based on student_id
    student = get_object_or_404(Students, student_id=student_id)
    # Fetch the marks associated with the student
    marks = Marks.objects.filter(student=student)
    # Render the template with student and marks data
    return render(request, 'student_marks.html', {'student': student, 'marks': marks})

