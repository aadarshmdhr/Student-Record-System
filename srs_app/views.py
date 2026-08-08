from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from srs_app.models import Student

# Create your views here.


def student_list(request):
    # Fetch all students from the database
    students = Student.objects.all()
    return render(
        request,
        "student_list.html",
        {"students": students},
    )


def delete_student(request, pk):
    # Fetch the student to be deleted
    student = Student.objects.get(pk=pk)
    student.delete()
    return HttpResponseRedirect("/")
