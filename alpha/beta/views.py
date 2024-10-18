from django.shortcuts import get_object_or_404, render, redirect
from .models import Student,Subject, Mark, Admin
from .forms import StudentForm
# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Search by id
def student_detail(request):
    student = None
    student_id = request.GET.get('student_id')  # Get student_id from the search form
    
    if student_id:
        try:
            student = Student.objects.get(student_id=student_id)  # Fetch the student by student_id
        except Student.DoesNotExist:
            student = None  # No student found with that ID
    
    return render(request, 'student_detail.html', {'student': student, 'student_id': student_id})

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list page after adding
    else:
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})

def delete_student(request):
    message = ''
    if request.method == 'POST':
        student_id = request.POST.get('student_id')  # Get the student_id from the form
        
        try:
            # Attempt to find the student and delete
            student = Student.objects.get(student_id=student_id)
            student.delete()
            message = f"Student with ID {student_id} has been successfully deleted."
        except Student.DoesNotExist:
            message = f"No student found with ID {student_id}."

    return render(request, 'delete_student.html', {'message': message})

def view_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'view_subjects.html', {'subjects': subjects})