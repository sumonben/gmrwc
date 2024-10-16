from django.shortcuts import render
from .forms import StudentForm,SubjectChoiceForm,AdressForm,SscEquvalentForm

# Create your views here.
def testHtml(request ):
    form = StudentForm()
    subject_form = SubjectChoiceForm()
    adress_form = AdressForm()
    ssc_equivalent_form=SscEquvalentForm()


    return render(request, 'admission/admission.html',{'form':form,'subject_form':subject_form,'adress_form':adress_form,'ssc_equivalent_form':ssc_equivalent_form})
