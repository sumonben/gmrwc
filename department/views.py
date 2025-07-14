from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from frontpage.models import Carousel,Page,NavItem,NavElement,Post,ServiceBox,Institute
from .models import Department,NavDepartment,NavDepartmentElement
from teacher.models import Teacher,Position
from student.models import Student
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Q,Count
from employee.models import Employee

def queryDepartmentFrontpage( departmentId ):
    carousels = Carousel.objects.all().order_by('cid')
    nav_department=NavDepartment.objects.all().order_by('serial') 
    institute=Institute.objects.filter(serial=1).first()
    principal=Teacher.objects.filter(position=1, release_date=None).first()
    vice_principal=Teacher.objects.filter(position=2, release_date=None).first()
    
    position=Position.objects.filter(serial=4).first()

    department=Department.objects.filter(id=departmentId).first()
    teachers=Teacher.objects.filter(~Q(position__serial=1),~Q(position__serial=2),t_department=department,release_date=None,is_active=True).order_by('t_department__serial','designation__serial','position__serial')
    students=Student.objects.filter(department=department,is_active=True)
    department_head=Teacher.objects.filter(t_department=department, position=position, release_date=None,is_active=True).first()
    notices=Post.objects.filter(category__name_en=department.name_en).order_by('-id')


    context = {
        'carousels': carousels,'nav_department':nav_department,'notices':notices,'department':department,
        'principal':principal,
        'institute':institute,
        'vice_principal':vice_principal,
        'department_head':department_head,
        }
    return context
    


def DepartmentPage(request, navitem_name,navelement_head,heading, id):

    #print(heading)
    heading=heading.replace("%20", " ")
    navitem_name=navitem_name.replace("%20", " ")
    navelement_head=navelement_head.replace("%20", " ")
    carousels = Carousel.objects.all().order_by('cid')
    navitems=NavItem.objects.all().order_by('serial')
    nav_department=NavDepartment.objects.all().order_by('serial') 
    #print(nav_department) 
    page=Page.objects.filter(id=id).distinct().first()
    institute=Institute.objects.filter(serial=1).first()
    notices=Post.objects.all().order_by('-id')
    principal=Teacher.objects.filter(position__serial=1, release_date=None).first()
    vice_principal=Teacher.objects.filter(position__serial=2, release_date=None).first()
    
    position=Position.objects.filter(serial=4).first()
    department=Department.objects.filter(name_en=heading).first()
    teachers=Teacher.objects.filter(t_department=department, release_date=None,is_active=True).filter((Q(position__serial=3)|Q(position__serial=4))).order_by('designation__serial','position__serial')
    students=Student.objects.filter(department=department,is_active=True)
    department_head=Teacher.objects.filter(t_department=department, position=position, release_date=None,is_active=True).first()
    #print("position: ",position.serial)
    #print("Department: ",department)

    print("Hello: ",department_head)

    context = {
        'carousels': carousels,'page':page,'navitems':navitems,'nav_department':nav_department,'notices':notices,
        'navitem_name':navitem_name,
        'heading':heading,
        'id':id,
        'principal':principal,
        'institute':institute,
        'vice_principal':vice_principal,
        'department_head':department_head,
        }
    
    context['department_head']=department_head
    context['department']=department

    '''books=Book.objects.all().select_related('author').order_by('-id')[:7]
    categories=Category.objects.all()
    tags=Tag.objects.all()
    authors=Author.objects.all()
    navitems=NavItem.objects.all()
    departments=Department.objects.all()
    publishers=Publisher.objects.all()
    subjects=Subject.objects.all()
    if type in 'category':
        allbooks = Book.objects.filter(category__id=id).order_by('-id').distinct()
    elif type in 'tag':
        allbooks = Book.objects.filter(tag__id=id).order_by('-id').distinct()
    elif type in 'publisher':
        allbooks = Book.objects.filter(publisher__id=id).order_by('-id').distinct()
    elif type in 'author':
        allbooks = Book.objects.filter(author__id=id).order_by('-id').distinct()
    elif type in 'department':
        allbooks = Book.objects.filter(department__id=id).order_by('-id').distinct()
    elif type in 'subject':
        allbooks = Book.objects.filter(subject__id=id).order_by('-id').distinct()
        
    page = request.GET.get('page', 1)
    paginator = Paginator(allbooks, 3)
    try:
         allbooks = paginator.page(page)
    except PageNotAnInteger:
         allbooks = paginator.page(1)
    except EmptyPage:
         allbooks = paginator.page(paginator.num_pages)    

    '''

    '''books=Book.objects.all().select_related('author').order_by('-id')[:7]
    categories=Category.objects.all()
    tags=Tag.objects.all()
    authors=Author.objects.all()
    navitems=NavItem.objects.all()
    departments=Department.objects.all()
    publishers=Publisher.objects.all()
    subjects=Subject.objects.all()
    if type in 'category':
        allbooks = Book.objects.filter(category__id=id).order_by('-id').distinct()
    elif type in 'tag':
        allbooks = Book.objects.filter(tag__id=id).order_by('-id').distinct()
    elif type in 'publisher':
        allbooks = Book.objects.filter(publisher__id=id).order_by('-id').distinct()
    elif type in 'author':
        allbooks = Book.objects.filter(author__id=id).order_by('-id').distinct()
    elif type in 'department':
        allbooks = Book.objects.filter(department__id=id).order_by('-id').distinct()
    elif type in 'subject':
        allbooks = Book.objects.filter(subject__id=id).order_by('-id').distinct()
        
    page = request.GET.get('page', 1)
    paginator = Paginator(allbooks, 3)
    try:
         allbooks = paginator.page(page)
    except PageNotAnInteger:
         allbooks = paginator.page(1)
    except EmptyPage:
         allbooks = paginator.page(paginator.num_pages)    

    '''
    
    return render(request,page.template.directory+'/'+page.template.name,context=context)

def departmentItems(request,departmentId,navitem_name):
    navitem_name=navitem_name.replace("%20", " ")    
    carousels = Carousel.objects.all().order_by('cid')
    nav_department=NavDepartment.objects.all().order_by('serial') 
    institute=Institute.objects.filter(serial=1).first()
    principal=Teacher.objects.filter(position=1, release_date=None).first()
    vice_principal=Teacher.objects.filter(position=2, release_date=None).first()
    position=Position.objects.filter(serial=4).first()
    department=Department.objects.filter(id=departmentId).first()
    teachers=Teacher.objects.filter(~Q(position__serial=1),~Q(position__serial=2),t_department=department,release_date=None,is_active=True).order_by('designation__serial','position__serial')
    students=Student.objects.filter(department=department,is_active=True)
    department_head=Teacher.objects.filter(t_department=department, position=position, release_date=None,is_active=True).first()
    employees=Employee.objects.filter(employee_department=department).order_by('designation','employee_type','position')
    notices=Post.objects.filter(category__name_en=department.name_en).order_by('-id')


    context = {
        'carousels': carousels,'nav_department':nav_department,'notices':notices,'department':department,
        'principal':principal,
        'navitem_name':navitem_name,
        'institute':institute,
        'vice_principal':vice_principal,
        'department_head':department_head,
        }
    print(navitem_name)
    if navitem_name == 'About': 
        context['About']='About'
    if navitem_name == 'Department  Head':
        context['teacher']=department_head
    
    if navitem_name=='Teachers-Officers': 
        context['teachers']=teachers
    if navitem_name=='Employees': 
        context['employees']=employees
    if navitem_name=='Students': 
        context['students']=students
    if navitem_name=='Seminar':
        post=Post.objects.filter(category__name_en=department.name_en).order_by('-id') 
        context['post']=post
    if navitem_name=='Results': 
        context['students']=students
    if navitem_name=='Seminar': 
        context['seminar']=students
    if navitem_name=='Results': 
        context['results']=students
    if navitem_name=='Notices': 
        post=Post.objects.filter(category__name_en=department.name_en).order_by('-id') 
        context['post']=post
    

    return render(request,"department/department.html",context=context)

@xframe_options_exempt
def singleNoticeDepartment(request, departmentId,id):
    context=queryDepartmentFrontpage(departmentId)
    post=Post.objects.filter(id=id).first()
    context['post']=post
    return render(request,"department/showpost_department.html",context=context)
