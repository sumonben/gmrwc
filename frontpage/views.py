from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Carousel,Page,NavItem,NavElement,Post,ServiceBox
from department.models import Department
# Create your views here.
class frontpage_view(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontpage/govtpage.html'
    def get(self, request):
        carousels = Carousel.objects.all().order_by('cid')
        pages = Page.objects.all().order_by('serial')
        navitems=NavItem.objects.all().order_by('serial')
        notices=Post.objects.all().order_by('-id')
        service_boxes=ServiceBox.objects.all().order_by('serial')

        #chapters = Chapter.objects.all
        #news = News.objects.all
        #chapters="sumon"
        #for chapter in singlepost:
        # print(chapter.name)
        #serializer = frontpageSerializer(carousel,many=True)
        return Response({ 'carousels': carousels,'pages':pages,'navitems':navitems,'notices':notices,'service_boxes':service_boxes})
def showPage(request, type,heading, id):

    carousels = Carousel.objects.all().order_by('cid')
    navitems=NavItem.objects.all().order_by('serial')  
    page=Page.objects.filter(id=id).distinct().first()
    notices=Post.objects.all().order_by('-id')
    departments=Department.objects.filter(name=heading).first()

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
    
    if(page.type=='1'):
        return render(request,'account/login.html',context=context)
    elif(page.type=='2'):
        return render(request,page.template.directory+'/'+page.template.name,context=context)
    else:
        return redirect(page.link)

