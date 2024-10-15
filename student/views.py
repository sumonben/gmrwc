from django.shortcuts import render
from .forms import StudentForm,SubjectChoiceForm

# Create your views here.
def testHtml(request ):
    form = StudentForm()
    subject_form = SubjectChoiceForm()

    return render(request, 'admission/admission.html',{'form':form,'subject_form':subject_form})
