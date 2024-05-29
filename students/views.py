from django.shortcuts import render, get_object_or_404
from students.models import Student
from django.http import  HttpResponse

# Create your views here.
def student_details(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
    }
    return render(request, 'student_detail.html', context)