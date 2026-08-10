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


def create_student(request):
    if request.method == "GET":
        return render(request, "create_student.html")
    else:
        Student.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            email=request.POST["email"],
        )
        return HttpResponseRedirect(("/"))


def update_student(request, id):
    if request.method == "GET":
        student = Student.objects.get(id=id)
        return render(
            request, 
            "update_student.html", 
            {"student": student}
        )
    else:
        student = Student.objects.get(id=id)
        student.name = request.POST["name"]
        student.age = request.POST["age"]
        student.email = request.POST["email"]
        student.save()
        return HttpResponseRedirect(("/"))
