from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Semester, Subject, Resource

def loginView(req):
    return render(req, 'logIn.html')
    
def signupView(req):
    return render(req, 'signUp.html')

def homePage(req):
    return render(req, 'navbar.html')

def viewPage(req):
    resources = Resource.objects.all()
    return render(req, 'view.html', context={
        "resources": resources
    })

def uploadPage(req):
    return render(req, 'upload.html')


def resourceSubmit(req):
    if req.method == "POST":
        course = req.POST.get('course')
        semester = int(req.POST.get('semester'))
        subjectId, subjectName = req.POST.get('subject').split(":")
        resourceType = req.POST.get('resourceType')
        resourceLink = req.POST.get('resourceLink')
        
        # add course if not present
        if not Course.objects.filter(course_name=course).exists():
            Course(course_name=course).save()
        else: print(course, "already exists!")
        
        # get course object
        courseObj = Course.objects.get(course_name=course)
        
        
        # add semester if not present
        if not Semester.objects.filter(course=courseObj, semester_number=semester).exists():
            Semester(course=courseObj, semester_number=semester).save()
        else: print(semester, "already exists!")
        
        # get semester object
        semesterObj = Semester.objects.get(course=courseObj, semester_number=semester)
        
        
        # add subject if not present
        if not Subject.objects.filter(semester=semesterObj, subject_code=subjectId, subject_name=subjectName).exists():
            Subject(semester=semesterObj, subject_code=subjectId, subject_name=subjectName).save()
        else: print(subjectId, "already exists!")
        
        # get subject object
        subjectObj = Subject.objects.get(semester=semesterObj, subject_code=subjectId, subject_name=subjectName)
        
        # add resources if not present
        if not Resource.objects.filter(subject=subjectObj, resource_link=resourceLink, resource_type=resourceType).exists():
            Resource(subject=subjectObj, resource_link=resourceLink, resource_type=resourceType).save()
        else: print("Resources already Exists!")
        
        print(course)
        print(semester)
        print(subjectId)
        print(subjectName)
        print(resourceType)
        print(resourceLink)
        
        
    return render(req, 'upload.html')