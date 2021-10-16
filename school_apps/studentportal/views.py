from django.shortcuts import get_object_or_404, render
from school_apps.admissions.models import Student
from .models import *
# Create your views here.


def myPortal(request, *args, **kwargs):
    student_profile = get_object_or_404(Student, user=request.user)

    context = {
        'student_profile':student_profile
    }
    return render(request, 'student-portal/main.html', context)