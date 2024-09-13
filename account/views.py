import json
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate,logout
from .forms import StudentForm,TeacherForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Student,Teacher
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
            user = UserModel.objects.create_user(username=username,
                                 email=email,last_name=last_name,
                                 password=password,is_active=False)
            user_form.user=user
            user_form.save()
            
            #messages.success(request, 'Student with name  {}  added.'.format(request.POST['name']))
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully'},safe=False)
        print(form.errors)
        return JsonResponse({'status': form.errors,'meaasge':'Account created Successfully'},safe=False)
        return render(request, 'account/register.html', {'form': form})
    return render(request, 'account/register.html', {'form': form}) 

@csrf_exempt
def Login(request):
    if request.method == 'GET': 
        context = ''
        if request.user.is_authenticated:
            return redirect("profile")
        return render(request, 'account/login.html', {'context': context})
    if request.method == 'POST':
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
    if request.user.is_authenticated:
        student=Student.objects.filter(user=request.user).first()
        print(student)
        return render(request, 'account/profile.html',{'student':student})
    else:
        return redirect('login')

@login_required
def Logout(request):
    logout(request)
    return redirect("login")