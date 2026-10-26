from django.shortcuts import render
from .models import Student


def student_list(request):
    # Retrieve student records from the SQLite database.
    students = Student.objects.all().order_by("roll_no")
    return render(request, "students/student_list.html", {"students": students})
