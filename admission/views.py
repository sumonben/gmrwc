from django.shortcuts import render
from student.forms import StudentForm

# Create your views here.
def admissionForm(request ):
    form = StudentForm()
    print(form)
    return render(request, 'admission/admission.html',{'form':form})
# Create your views here.
