from django.contrib import admin
from .models import Resource, Course, Semester, Subject

@admin.register(Resource)
class ResourceModelAdmin(admin.ModelAdmin):
    list_display = ['course_','semester_','subject','resource_type']
    def course_(self, obj):
        return obj.subject.semester.course
    def semester_(self, obj):
        return obj.subject.semester.semester_number
    
admin.site.register(Course)

@admin.register(Semester)
class SemesterModelAdmin(admin.ModelAdmin):
    list_display = ['course','semester_number']


@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'subject_name', 'semester_', "course_"]
    
    def semester_(self, obj):
        sem = obj.semester.semester_number
        return sem
        
    def course_(self, obj):
        cr = obj.semester.course.course_name
        return cr
