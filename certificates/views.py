from django.shortcuts import render
from student.forms import SscEquvalentForm,SubjectChoiceForm,AdressForm
from .forms import ChoiceCertificateForm,CertificateForm
from department.models import Group
# Create your views here.

def ChoiceCertificate(request):
    form=ChoiceCertificateForm()
    return render(request,'certificate/choice_certificate.html',{'form':form})
def CertificateFormEntry(request):
    print(request.POST.get('student_category'))
    group=Group.objects.filter(id=request.POST.get('group')).first()
    print(group.title_en)
    form=CertificateForm()
    adress_form = AdressForm()
    context={'form':form,'adress_form':adress_form}
    subject_form=SubjectChoiceForm(group=group)
    if request.POST.get('student_category') in '3':
        context['subject_form']=subject_form
        return render(request,'certificate/certificate_form_entry_hsc.html',context=context)
    return render(request,'certificate/certificate_form_entry_all.html',context=context)
  


    