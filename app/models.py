from django.db import models
from django.contrib.auth.models import User



# choices of course_name
COURSE_CHOICES = (
    ("MCA", "MCA"),
    ("BTECH-CSE", "BTECH-CSE"),
    ("BTECH-ECE", "BTECH-ECE"),
    ("BTECH-EE", "BTECH-EE"),
    ("BTECH-ME", "BTECH-ME"),
)


# create course table
class Course(models.Model):
    course_name = models.CharField(max_length=100, choices=COURSE_CHOICES)

    def __str__(self):
        return self.course_name


# choices of semester
SEMESTER_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
)


# create course semester
class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_number = models.IntegerField(choices=SEMESTER_CHOICES)

    def __str__(self):
        return str(self.course) + "-" + str(self.semester_number)


# create subject table
class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.subject_code} ({self.subject_name})"


# choices of types
RESOURCES_TYPE_CHOICES = (
    ("PYQ", "PYQ"),
    ("Reading Material", "Reading Material"),
    ("Online Resources", "Online Resources")       
)


# create resources table
class Resource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    resource_link = models.CharField(max_length=1000)
    resource_type = models.CharField(max_length=1000, choices=RESOURCES_TYPE_CHOICES)

    def __str__(self):
        return self.resource_type
