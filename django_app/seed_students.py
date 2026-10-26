import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_project.settings")
django.setup()

from students.models import Student

sample_students = [
    {"roll_no": 101, "name": "Aman", "branch": "CSE", "marks": 85},
    {"roll_no": 102, "name": "Priya", "branch": "ECE", "marks": 91},
    {"roll_no": 103, "name": "Rahul", "branch": "IT", "marks": 78},
]

for item in sample_students:
    Student.objects.get_or_create(roll_no=item["roll_no"], defaults=item)

print("Sample student records inserted (where missing).")
