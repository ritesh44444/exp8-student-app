from django.db import models


class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
