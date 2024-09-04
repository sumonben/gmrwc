from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate,logout
from .forms import StudentForm
# Create your views here.
UserModel=get_user_model()
def Registration(request):
    context ={}

    form = StudentForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request,'account/register.html',context=context)

def Login(request):
    if request.method == 'GET':
        context = ''
        if request.user.is_authenticated:
            return HttpResponse("Sumon")
        return render(request, 'account/login.html', {'context': context})
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        
        if UserModel.objects.filter(email=email).exists() is False:
            email='Email not exist in user system!! '
            return render(request, 'accounts/login.html', {'email': email})

        user = authenticate(request, username=email, password=password)
        if user is not None:
            error=login(request, user)
            print(error)
            return redirect('login')
            # Redirect to a success page.
            ...
        else:
            
            password='Your Creadentials do not match, Please try again!!'
            return render(request, 'account/login.html', {'password': password})


def Profile(request):
    return render(request, 'account/profile.html',)