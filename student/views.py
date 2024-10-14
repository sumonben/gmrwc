from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def testHtml(request ):
    form = StudentForm()
    print(form)
    return render(request, 'admission/admission.html',{'form':form})
