from django.shortcuts import redirect, render
from .forms import StudentForm,SubjectChoiceForm,AdressForm,SscEquvalentForm,GuardianForm,PresentAdressForm
from department.models import Group,Subject
from django.db.models import Q,Count

# Create your views here.
def testHtml(request ):
        print("hello")
        group=Group.objects.filter(title_en="Business Studies").first()
        form = StudentForm()
        if group:
            subject_form = SubjectChoiceForm(group=group)
        else:
            subject_form = None

        adress_form = AdressForm()
        present_adress_form = PresentAdressForm()

        ssc_equivalent_form=SscEquvalentForm()
        guardian_form=GuardianForm()


        return render(request, 'admission/admission.html',{'form':form,'subject_form':subject_form,'adress_form':adress_form,'ssc_equivalent_form':ssc_equivalent_form,'guardian_form':guardian_form,'present_adress_form':present_adress_form})
