from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from frontpage.models import Carousel,Page,NavItem,NavElement,Post,ServiceBox
from .models import Department

# Create your views here.
def DepartmentPage(request, type,heading, id):

    carousels = Carousel.objects.all
    navitems=NavItem.objects.all    
    page=Page.objects.filter(id=id).distinct().first()
    notices=Post.objects.all().order_by('-id')
    departments=Department.objects.filter(name=heading).first()
    print(departments.id)
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
    context = {
        'carousels': carousels,'page':page,'navitems':navitems,'notices':notices,
        'type':type,
        'heading':heading,
        'id':id,


     }
     #   return render(request,'postview/showpost.html',context=context)
    
    #return render(request,page.template.directory+'/'+page.template.name,context=context)
    return render(request,page.template.directory+'/'+page.template.name,context=context)


