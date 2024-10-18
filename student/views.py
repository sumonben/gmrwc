from django.shortcuts import render
from .forms import StudentForm,SubjectChoiceForm,AdressForm,SscEquvalentForm,GuardianForm,PresentAdressForm

# Create your views here.
def testHtml(request ):
    form = StudentForm()
    subject_form = SubjectChoiceForm()
    adress_form = AdressForm()
    present_adress_form = PresentAdressForm()

    ssc_equivalent_form=SscEquvalentForm()
    guardian_form=GuardianForm()


    return render(request, 'admission/admission.html',{'form':form,'subject_form':subject_form,'adress_form':adress_form,'ssc_equivalent_form':ssc_equivalent_form,'guardian_form':guardian_form,'present_adress_form':present_adress_form})
