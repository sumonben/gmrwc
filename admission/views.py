from django.http import JsonResponse
from django.shortcuts import render,redirect
from student.forms import StudentForm,AdressForm,PresentAdressForm,SscEquvalentForm,SubjectChoiceForm,GuardianForm
from student.models import Group
# Create your views here.
def admissionLogin(request ):
    form = StudentForm()
    #print(form)
    return render(request, 'admission/admission_login.html',{'form':form})
# Create your views here.
# Create your views here.
def admissionForm(request ):
    if request.method=="POST":
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
    return redirect('admission_login')


def admissionFormSubmit(request):
    if request.method=='POST':
        print(request.POST.get('name'))
    return JsonResponse({'status': 'success','meaasge':'Account created Successfully'},safe=False)
