from django.utils.encoding import uri_to_iri
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from urllib.parse import urlencode
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Carousel,Page,NavItem,NavElement,Post,ServiceBox,Institute
from department.models import Department
from teacher.models import Teacher
from student.models import Student
from student.forms import StudentForm
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Q,Count

# Create your views here.
class frontpage_view(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontpage/govtpage.html'
    def get(self, request):
        carousels = Carousel.objects.all().order_by('cid')
        institute=Institute.objects.first()
        pages = Page.objects.all().order_by('serial')
        navitems=NavItem.objects.all().order_by('serial')
        notices=Post.objects.all().order_by('-id')[:7]
        service_boxes=ServiceBox.objects.all().order_by('serial')
        principal=Teacher.objects.filter(position__serial=1, release_date=None,is_active=True).first()   
        vice_principal=Teacher.objects.filter(position__serial=2, release_date=None,is_active=True).first()
        print(principal)
        #chapters = Chapter.objects.all
        #news = News.objects.all
        #chapters="sumon"
        #for chapter in singlepost:
        # print(chapter.name)
        #serializer = frontpageSerializer(carousel,many=True)
        return Response({ 'carousels': carousels,'pages':pages,'navitems':navitems,'notices':notices,'service_boxes':service_boxes,'principal':principal,'viec_principal':vice_principal,'institute':institute})
def queryFrontpage():
    institute=Institute.objects.first()
    carousels = Carousel.objects.all().order_by('cid')
    navitems=NavItem.objects.all().order_by('serial')
    notices=Post.objects.all().order_by('-id')[:7]
    principal=Teacher.objects.filter(position__serial=1, release_date=None,is_active=True).first()   
    vice_principal=Teacher.objects.filter(position__serial=2, release_date=None,is_active=True).first()
    teachers=Teacher.objects.filter(release_date=None,is_active=True).annotate(count=Count('t_department')).order_by().order_by('designation__serial','position__serial')
    academic_council=Teacher.objects.filter(Q(position__serial=4)|Q(position__serial=1)|Q(position__serial=2), release_date=None,is_active=True).order_by('designation__serial','position__serial')
    context = {
        'institute':institute,
        'carousels': carousels,
        'navitems':navitems,
        'notices':notices,
        'principal':principal,
        'institute':institute,
        'viec_principal':vice_principal,
        'academic_council':academic_council,
        }
    return context
    


    

def languageChange(request):
    print('1',request.POST.get('lang_toggle', False))
    if 'lang' not in request.session:
        request.session['lang']='bangla'
        print('2',request.session['lang'])
        del request.session['lang']
    if request.POST.get('lang_toggle', False) == 'english':
        request.session['lang']='english'
        print('3',request.session['lang'])
    else:
        request.session['lang']='bangla'

    return JsonResponse({'success': "success"},safe=False)


def showPage(request, navitem_name,navelement_head,heading, id):
    teacher=None
    heading=heading.replace("%20", " ")
    navitem_name=navitem_name.replace("%20", " ")
    navelement_head=navelement_head.replace("%20", " ")
    #print("Test: "+heading.replace("%20", " "))
    carousels = Carousel.objects.all().order_by('cid')
    institute=Institute.objects.first()
    navitems=NavItem.objects.all().order_by('serial')
    navitem=NavItem.objects.filter(name_en=navitem_name).first()
    navelement=NavElement.objects.filter(head_en=navelement_head).first() 
    page=Page.objects.filter(id=id).distinct().first()
    post=page
    notices=Post.objects.all().order_by('-id')[:7]
    principal=Teacher.objects.filter(position__serial=1, release_date=None,is_active=True).first()   
    vice_principal=Teacher.objects.filter(position__serial=2, release_date=None,is_active=True).first()
    teachers=Teacher.objects.filter(release_date=None,is_active=True).annotate(count=Count('t_department')).order_by().order_by('designation__serial','position__serial')
    academic_council=Teacher.objects.filter(Q(position__serial=4)|Q(position__serial=1)|Q(position__serial=2), release_date=None,is_active=True).order_by('designation__serial','position__serial')
    context = {
        'carousels': carousels,'page':page,'navitems':navitems,'notices':notices,
        'navitem_name':navitem_name,
        'navitem':navitem,
        'heading':heading,
        'id':id,
        'navelement_head':navelement_head,
        'navelement':navelement,
        'principal':principal,
        'institute':institute,
        'viec_principal':vice_principal,
        'academic_council':academic_council,
        }
    #if navelement_head=="HSC" and heading=="Admission Notice" :
    post=Post.objects.filter(category__name_en=navelement_head,tag__name_en=heading)
    context['post']=post
    
    '''if navelement_head=="HSC" and heading=="Admission Application" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Admission Application")
        context['post']=post
    if navelement_head=="HSC" and heading=="Form Fill-up(Exams)" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Form Fill-up(Exams)")
        context['post']=post
    if navelement_head=="HSC" and heading=="Results( Internal )" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Results( Internal )")
        context['post']=post
    if navelement_head=="HSC" and heading=="Results (Board)" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Results (Board)")
        context['post']=post
    if navelement_head=="Honors" and heading=="Admission Notice" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Admission Notice")
        context['post']=post
    if navelement_head=="Honors" and heading=="Admission Application" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Admission Application")
        context['post']=post
    if navelement_head=="Honors" and heading=="Exams Notice" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Exams Notice")
        context['post']=post
    if navelement_head=="Honors" and heading=="ভর্তি আবেদন" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="ভর্তি আবেদন")
        context['post']=post
    if navelement_head=="Honors" and heading=="Form Fill-up(Exams)" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Form Fill-up(Exams)")
        context['post']=post
    if navelement_head=="Honors" and heading=="Results ( National University)" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Results ( National University)")
        context['post']=post
        print(post)
    if navelement_head=="Masters" and heading=="Admission Notice" :
        post=Post.objects.filter(category__name_en="Masters",tag__name_en="Admission Notice")
        context['post']=post
    if navelement_head=="Masters" and heading=="Admission Application" :
        post=Post.objects.filter(category__name_en="Masters",tag__name_en="Admission Application")
        context['post']=post
    if navelement_head=="Masters" and heading=="Exams Notice" :
        post=Post.objects.filter(category__name_en="Masters",tag__name_en="Exams Notice")
        context['post']=post
    if navelement_head=="Masters" and heading=="Results ( National University)" :
        post=Post.objects.filter(category__name_en="Masters",tag__name_en="Results ( National University)")
        context['post']=post
    if navelement_head=="Degree (Pass)" and heading=="Admission Notice" :
        post=Post.objects.filter(category__name_en="Degree (Pass)",tag__name_en="Admission Notice")
        context['post']=post
    if navelement_head=="Degree (Pass)" and heading=="Admission Application" :
        post=Post.objects.filter(category__name_en="Degree (Pass)",tag__name_en="Admission Application")
        context['post']=post
    if navelement_head=="Degree (Pass)" and heading=="Exams Notice" :
        post=Post.objects.filter(category__name_en="Degree (Pass)",tag__name_en="Exams Notice")
        context['post']=post
    if navelement_head=="Degree (Pass)" and heading=="Results ( National University)" :
        post=Post.objects.filter(category__name_en="Degree (Pass)",tag__name_en="Results ( National University)")
        context['post']=post
    '''
        
    if heading =='Principal':
        context['teacher'] = principal

    
    if heading =='Vice-Principal':
        context['teacher'] = vice_principal

    if heading =='Academic Council':
        context['teachers'] = academic_council
    
    if heading =='Teachers':
        context['teachers'] = teachers
    

    

    
    
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
    
    
    if(page.type=='1' or navitem_name=='Online Classes'):
        return render(request,'postview/showpage.html',context=context)
    elif(page.type=='2'):
        return render(request,page.template.directory+'/'+page.template.name,context=context)
    else:
        return redirect(page.link)

def showServiceBoxItem(request, servicebox_id ,servicebox_title,heading, id):
    teacher=None
    carousels = Carousel.objects.all().order_by('cid')
    institute=Institute.objects.first()
    navitems=NavItem.objects.all().order_by('serial')  
    page=Page.objects.filter(id=id).distinct().first()
    notices=Post.objects.all().order_by('-id')[:7]
    principal=Teacher.objects.filter(position__serial=1, release_date=None,is_active=True).first()   
    vice_principal=Teacher.objects.filter(position__serial=2, release_date=None,is_active=True).first()
    teachers=Teacher.objects.filter( release_date=None,is_active=True)
    academic_council=Teacher.objects.filter(Q(position__serial=4)|Q(position__serial=1)|Q(position__serial=2), release_date=None,is_active=True)
    print(servicebox_title,heading)
    context = {
        'carousels': carousels,'page':page,'navitems':navitems,'notices':notices,
        'servicebox_title':servicebox_title,
        'heading':heading,
        'id':id,
        'principal':principal,
        'institute':institute,
        'viec_principal':vice_principal,
        'academic_council':academic_council,
        }
    if heading =='Principal':
        context['teacher'] = principal

    
    if heading =='Vice-Principal':
        context['teacher'] = vice_principal

    if heading =='Academic Council':
        context['teachers'] = academic_council
    
    if heading =='Teachers':
        context['teachers'] = teachers
        
    if servicebox_title=="Admission Guidelines" and heading=="HSC Admission" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Admission Notice")
        context['post']=post
        print(post)

    
    if servicebox_title=="Admission Guidelines" and heading=="Honors Admission" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Admission Notice")
        context['post']=post
    if servicebox_title=="Admission Guidelines" and heading=="Masters Admission" :
        post=Post.objects.filter(category__name_en="Masters",tag__name_en="Admission Notice")
        context['post']=post
    if servicebox_title=="Admission Guidelines" and heading=="Degree (Pass) Admission" :
        post=Post.objects.filter(category__name_en="Degree (Pass)",tag__name_en="Admission Notice")
        context['post']=post
    if servicebox_title=="Exams" and heading=="Board Exam (HSC)" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Results (Board)")
        context['post']=post
    if servicebox_title=="Exams" and heading=="Internal Exams (HSC)" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Exams (Internal)")
        context['post']=post
    if servicebox_title=="Exams" and heading=="Degree and Others" :
        post=Post.objects.filter(category__name_en="Degree (Pass)",tag__name_en="Exams (Degree Pass)")
        context['post']=post
    if servicebox_title=="Exams" and heading=="Exams (National University)" :
        post=Post.objects.filter(category__name_en="National University",tag__name_en="Exams (National University)")
        context['post']=post
    if servicebox_title=="Exams" and heading=="Exams (National University)" :
        post=Post.objects.filter(category__name_en="National University",tag__name_en="Exams (National University)")
        context['post']=post
    
    if servicebox_title=="Results" and heading=="Results ( Board Exams)" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Results (Board)")
        context['post']=post
    if servicebox_title=="Results" and heading=="Internal Results (HSC)" :
        post=Post.objects.filter(category__name_en="HSC",tag__name_en="Results (Internal )")
        context['post']=post
    if servicebox_title=="Results" and heading=="Results (National University)" :
        post=Post.objects.filter(category__name_en="National University",tag__name_en="Results ( National University)")
        context['post']=post
    if servicebox_title=="Results" and heading=="Internal Results (Honors)" :
        post=Post.objects.filter(category__name_en="National University",tag__name_en="Results ( National University)")
        context['post']=post
    
    if servicebox_title=="Honors" and heading=="Exams Notice" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Exams Notice")
        context['post']=post
    if servicebox_title=="Honors" and heading=="Admission Application" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Admission Application")
        context['post']=post
    if servicebox_title=="Honors" and heading=="Form Fill-up(Exams)" :
        post=Post.objects.filter(category__name_en="Honors",tag__name_en="Form Fill-up(Exams)")
        context['post']=post
    if servicebox_title=="Online Classes":
        navitem=NavItem.objects.filter(name_en='Online Classes').first()
        context['navitem']=navitem


    if(page.type=='1'):
        return render(request,'postview/showpage.html',context=context)
    elif(page.type=='2'):
        return render(request,page.template.directory+'/'+page.template.name,context=context)
    else:
        return redirect(page.link)


def tableAllShow(request, tableall ):
    carousels = Carousel.objects.all().order_by('cid')
    institute=Institute.objects.first()
    navitems=NavItem.objects.all().order_by('serial')
    notices=Post.objects.all().order_by('-id')[:7]
    principal=Teacher.objects.filter(position__serial=1, release_date=None,is_active=True).first()   
    vice_principal=Teacher.objects.filter(position__serial=2, release_date=None,is_active=True).first()
    teachers=Teacher.objects.filter( release_date=None,is_active=True)
    academic_council=Teacher.objects.filter(Q(position__serial=4)|Q(position__serial=1)|Q(position__serial=2), release_date=None,is_active=True)
    post=Post.objects.all().order_by('-id')
    context = {
        'carousels': carousels,'navitems':navitems,'notices':notices,
        'principal':principal,
        'institute':institute,
        'viec_principal':vice_principal,
        'academic_council':academic_council,
        'post':post,
        'teachers':teachers,

        }
    
    return render(request,'postview/notice_all_show.html',context=context)

@xframe_options_exempt
def singleNotice(request, id):
    context=queryFrontpage()
    post=Post.objects.filter(id=id).first()
    context['post']=post
    return render(request,"postview/showpost.html",context=context)

def testHtml(request ):
    form=StudentForm()
    return render(request, 'admission/filter_horizontal.html',{'form':form})
