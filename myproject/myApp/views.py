from django.shortcuts import render
from .models import Student
# Create your views here.
def index(req):
    student= Student.objects.all()
    context= {
        "student": student
    }
    return render(req, "index.html", context)