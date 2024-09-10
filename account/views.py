import json
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate,logout
from .forms import StudentForm,TeacherForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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

        #form_teacher = TeacherForm(request.POST)
        data = {}
        if request.POST.get('student'):
            form = StudentForm(request.POST, request.FILES)
            email=request.POST.get('email')
            username=request.POST.get('phone')
            password='Student@'+request.POST.get('phone')

        if request.POST.get('teacher'):
            form = TeacherForm(request.POST, request.FILES)
            email=request.POST.get('email')
            username=request.POST.get('service_id')
            password='Teacher@'+request.POST.get('service_id')
            print("sumon"+request.POST.get('teacher'))


        data['message']="Not Success"
        
        if form.is_valid():
            data['message']="Successfully Done"
            user_form=form.save(commit=False)
            user = UserModel.objects.create_user(username=username,
                                 email=email,
                                 password=password,is_active=False)
            user_form.user=user
            user_form.save()
            
            #messages.success(request, 'Student with name  {}  added.'.format(request.POST['name']))
            return JsonResponse({'status': 'success'},safe=False)
        print(form.errors)
        return render(request, 'account/register.html', {'form': form})
    return render(request, 'account/register.html', {'form': form}) 

def Login(request):
    if request.method == 'GET':
        context = ''
        if request.user.is_authenticated:
            return redirect("profile")
        return render(request, 'account/login.html', {'context': context})
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        
        if UserModel.objects.filter(email=email).exists() is False:
            email='Email not exist in user system!! '
            return render(request, 'account/login.html', {'email': email})

        user = authenticate(request, username=email, password=password)
        if user is not None:
            error=login(request, user)
            return redirect('profile')
            # Redirect to a success page.
            ...
        else:
            password='Your Creadentials do not match, Please try again!!'
            return render(request, 'account/login.html', {'password': password})

def Profile(request):
    if request.user.is_authenticated:
        return render(request, 'account/profile.html',)
    else:
        return redirect('login')