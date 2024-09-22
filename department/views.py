from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from frontpage.models import Carousel,Page,NavItem,NavElement,Post,ServiceBox
from .models import Department
from account.models import Teacher,Student


# Create your views here.
def DepartmentPage(request, navitem_name,navelement_head,heading, id):

    print("Sumon"+heading)
    carousels = Carousel.objects.all().order_by('cid')
    navitems=NavItem.objects.all().order_by('serial')  
    page=Page.objects.filter(id=id).distinct().first()
    print(page.category.all())
    notices=Post.objects.all().order_by('-id')
    principal=Teacher.objects.filter(position='অধ্যক্ষ', release_date=None).first()
    viec_principal=Teacher.objects.filter(position='উপাধ্যক্ষ', release_date=None).first()
    context = {
        'carousels': carousels,'page':page,'navitems':navitems,'notices':notices,
        'navitem_name':navitem_name,
        'heading':heading,
        'id':id,
        'principal':principal,
        'viec_principal':viec_principal,
        }
    
    if heading in 'বিভাগীয় প্রধান':
        department_head=Teacher.objects.filter(position='বিভাগীয় প্রধান', release_date=None)

    print("department_head")

    department=Department.objects.filter(name=heading).first()
    teachers=Teacher.objects.filter(t_department=department, release_date=None,is_active=True)
    students=Student.objects.filter(department=department,is_active=True)
    department_head=Teacher.objects.filter(t_department=department, position='বিভাগীয় প্রধান', release_date=None,is_active=True).first()
    context = {
        'carousels': carousels,'page':page,'navitems':navitems,'notices':notices,
        'type':type,
        'heading':heading,
        'id':id,
        'principal':principal,
        'viec_principal':viec_principal,
        'department_head':department_head,
        }
    
    context['teachers']=teachers
    context['students']=students
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


