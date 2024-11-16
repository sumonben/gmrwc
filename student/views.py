from django.shortcuts import redirect, render
from .forms import StudentForm,SubjectChoiceForm,AdressForm,SscEquvalentForm,GuardianForm,PresentAdressForm
from department.models import Group,Subject
from .models import Student,SubjectChoice,SscEquvalent
from django.db.models import Q,Count
from payment.sslcommerz import sslcommerz_payment_gateway
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,HttpResponseNotFound


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

def certificateGenerate(request,id ,type ):
        student=Student.objects.filter(id=id).first()
        form = StudentForm()
        adress_form = AdressForm()
        guardian_form=GuardianForm()

        return render(request, 'account/profile.html',{'student':student,'form':form, 'adress_form':adress_form, 'guardian_form':guardian_form,})

def getCertificate(request):
    print("sumon")
    if request.user.is_authenticated:
        student=Student.objects.filter(user=request.user).first()
        subject_choice=SubjectChoice.objects.filter(student=student).first()
        if student.exam_roll:
            student.exam_roll=request.POST.get('exam_roll')
        if student.registration:
            student.registration=request.POST.get('registration_no')
        if student.guardian_info:
            student.guardian_info.father_name_en=request.POST.get('father_name')
        if student.guardian_info:   
            student.guardian_info.father_name_en=request.POST.get('mother_name')
        if request.POST.get('passing_year'):
            student.passing_year=request.POST.get('passing_year')
        if request.POST.get('cgpa'):
            student.cgpa=request.POST.get('cgpa')

        ssc_equivalent=SscEquvalent.objects.filter(student=student).first()

        return redirect(sslcommerz_payment_gateway(request,student.name, 100,student.phone))

        #print(response)
        #return render(request, 'student/testimonial.html',{'student':student,'ssc_equivalent':ssc_equivalent,'subject_choice':subject_choice})
    return render(request, 'account/login.html')

def getTestimonial(request):
    if request.user.is_authenticated:
        student=Student.objects.filter(user=request.user).first()
        print(student.name)
        subject_choice=SubjectChoice.objects.filter(student=student).first()
        
        ssc_equivalent=SscEquvalent.objects.filter(student=student).first()

        return render(request, 'student/testimonial.html',{'student':student,'ssc_equivalent':ssc_equivalent,'subject_choice':subject_choice})
    return render(request, 'account/login.html')
