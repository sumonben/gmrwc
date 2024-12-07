import json
import os
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate,logout
from .forms import StudentForm,TeacherForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from teacher.models import Teacher
from student.models import Student,SubjectChoice,SscEquvalent,GuardianInfo
from io import BytesIO
from django.http import FileResponse
from django.template.loader import get_template
# Create your views here.
UserModel=get_user_model()

@csrf_exempt
def Registration(request):
    context ={}
    
    if request.method == 'GET':
        form = StudentForm()
        form_teacher = TeacherForm()
        context={
            'form':form,

            'form_teacher':form_teacher,

        }
        return render(request,'account/register.html',context=context)

    if request.method == 'POST':

        context ={}

        data = {}
        if request.POST.get('student'):
            form = StudentForm(request.POST, request.FILES)
            email=request.POST.get('email')
            username=request.POST.get('phone')
            last_name='student'
            password='Student@'+request.POST.get('phone')
            print('0',email,username)

        if request.POST.get('teacher'):
            form = TeacherForm(request.POST, request.FILES)
            email=request.POST.get('t_email')
            username=request.POST.get('t_phone')
            last_name='teacher'
            password='Teacher@'+request.POST.get('t_phone')
            print("sumon"+request.POST.get('teacher'))
        if UserModel.objects.filter(email=email).exists() is True:
            email='Email already exist in user system!! '
            context['email']=email
            print('1',email,username)
            
        if UserModel.objects.filter(username=username).exists() is True:
            phone='Phone number already exist in user system!! '
            context['phone']=phone
            print('2',email,username)
            
        if bool(context):
            print('5',email,username)
            return JsonResponse({'context': context},safe=False)


        data['message']="Not Success"
        
        if form.is_valid():
            print('4',email,username)
            data['message']="Successfully Done"
            user_form=form.save(commit=False)
            if request.POST.get('teacher'):
                positions=form.cleaned_data['position']
                branchs=form.cleaned_data['branch']
                user_form.save()
                for i in positions:
                    user_form.position.add(i)
                for i in branchs:
                    user_form.branch.add(i)
                user_form.save()
 

            user = UserModel.objects.create_user(username=username,
                                 email=email,last_name=last_name,
                                 password=password,is_active=False)
            #print(user_form.student_category)

            user_form.user=user
            user_form.save()
            

            
            #messages.success(request, 'Student with name  {}  added.'.format(request.POST['name']))
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully'},safe=False)
        print(form.errors)
        return JsonResponse({'status': form.errors,'meaasge':'Account Not Created'},safe=False)
    return render(request, 'account/register.html', {'form': form}) 

@csrf_exempt
def Login(request):
    if request.method == 'GET': 
        context = ''
        if request.user.is_authenticated:
            return redirect("profile")
        return render(request, 'account/login.html', {'context': context})
    if request.method == 'POST':
        print("Got Login")
        email = request.POST['email']
        password = request.POST['email_password']
        
        if UserModel.objects.filter(email=email).exists() is False:
            email='email'
            print(email)
            return JsonResponse({'email': email},safe=False)


        user = authenticate(request, username=email, password=password)
        if user is not None:
            error=login(request, user)
            return JsonResponse({'success': "success"},safe=False)
            # Redirect to a success page.
            ...
        else:
            password='password'
            return JsonResponse({'password': password},safe=False)

def Profile(request):
    if request.user.is_authenticated and request.user.is_active :
        print(request.user.email)
        email=request.user.email
        if request.user.last_name in 'student':
            student=Student.objects.filter(user=request.user).first()
            print(student)
            return render(request, 'account/profile.html',{'student':student})
        if request.user.last_name in 'teacher':
            teacher=Teacher.objects.filter(user=request.user).first()
            print(teacher)
            return render(request, 'account/teacherprofile.html',{'teacher':teacher})
        return render(request, 'account/profile.html')
    

    else:
        return redirect('login')

@login_required
def Logout(request):
    logout(request)
    return redirect("login")


 
 
def generate_pdf(request):
    if request.user.is_authenticated:
        student=Student.objects.filter(user=request.user).first()
        subject_choice=SubjectChoice.objects.filter(student=student).first()
        
        ssc_equivalent=SscEquvalent.objects.filter(student=student).first()

        return render(request, 'admission/admission_form.html',{'student':student,'ssc_equivalent':ssc_equivalent,'subject_choice':subject_choice})
    return render(request, 'account/login.html')
        

        

    
    
    
    
    
    
    ''''student=Student.objects.filter(user=request.user).first()
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gmrwc_logo.jpg')
    response = render_to_pdf("account/certificate.html",{'student':student,'image':fn})
    if response.status_code == 404:
        raise HttpResponseNotFound("Statement form not found.")

    filename = "Statement_form.pdf"
    content = f"inline; filename={filename}"
    content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('utf-8')), result)
    if pdf.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    return HttpResponse(result.getvalue(), content_type='application/pdf')

def generate_pdf_file(request):
    
    student=Student.objects.filter(user=request.user).first()

    buffer = BytesIO()
    p = canvas.Canvas(buffer,pagesize=A4)
    
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gmrwc_logo.jpg')
    # Create a PDF document
    print(fn)
    p.drawImage(fn, 50, 760, width=60, height=60)    
    p.drawString(120,800, "Govt Mujibur Rahman Women's College")
    p.line(0,750,1000,750)
    p.drawString(100, 750, "Book Catalog")
    student=Student.objects.filter(user=request.user).first()

    y = 700
    p.drawString(100, y, f"নাম(বাংলা): {student.name_bangla}")
    p.drawString(100, y - 20, f"Name: {student.name}")
    p.drawString(100, y - 40, f"গ্রুপ: {student.group}")
    y -= 60
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer'''