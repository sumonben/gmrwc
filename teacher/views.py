from django.shortcuts import render

# Create your views here.
def teacher(request):
    return render("teacher/teacher_details.html")