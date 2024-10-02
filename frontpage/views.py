from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Carousel,Page,NavItem,NavElement,Post,ServiceBox,Institute
from department.models import Department
from teacher.models import Teacher
from student.models import Student

from django.db.models import Q

# Create your views here.
class frontpage_view(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontpage/govtpage.html'
    def get(self, request):
        carousels = Carousel.objects.all().order_by('cid')
        institute=Institute.objects.first()
        pages = Page.objects.all().order_by('serial')
        navitems=NavItem.objects.all().order_by('serial')
        notices=Post.objects.all().order_by('-id')
        service_boxes=ServiceBox.objects.all().order_by('serial')
        
        principal=Teacher.objects.filter(position=1, release_date=None).first()
        viec_principal=Teacher.objects.filter(position=2, release_date=None).first()
        #chapters = Chapter.objects.all
        #news = News.objects.all
        #chapters="sumon"
        #for chapter in singlepost:
        # print(chapter.name)
        #serializer = frontpageSerializer(carousel,many=True)
        return Response({ 'carousels': carousels,'pages':pages,'navitems':navitems,'notices':notices,'service_boxes':service_boxes,'principal':principal,'viec_principal':viec_principal,'institute':institute})

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
    carousels = Carousel.objects.all().order_by('cid')
    institute=Institute.objects.first()
    navitems=NavItem.objects.all().order_by('serial')
    navitem=NavItem.objects.filter(name=navitem_name).first()
    navelement=NavElement.objects.filter(head=navelement_head).first() 
    page=Page.objects.filter(id=id).distinct().first()
    notices=Post.objects.all().order_by('-id')
    principal=Teacher.objects.filter(position=1, release_date=None,is_active=True).first()   
    vice_principal=Teacher.objects.filter(position=2, release_date=None,is_active=True).first()
    teachers=Teacher.objects.filter( release_date=None,is_active=True)
    academic_council=Teacher.objects.filter(Q(position=4)|Q(position=1)|Q(position=2), release_date=None,is_active=True)

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
    if navelement_head=="এইচএসসি" and heading=="ভর্তি বিজ্ঞপ্তি" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
    
    if navelement_head=="এইচএসসি" and heading=="ভর্তি আবেদন" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ভর্তি আবেদন")
        context['post']=post
    if navelement_head=="এইচএসসি" and heading=="পরীক্ষার ফর্ম পূরণ " :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="পরীক্ষার ফর্ম পূরণ ")
        context['post']=post
    if navelement_head=="এইচএসসি" and heading=="ফলাফল (অভ্যন্তরীণ)" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ফলাফল (অভ্যন্তরীণ)")
        context['post']=post
    if navelement_head=="এইচএসসি" and heading=="ফলাফল (বোর্ড)" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ফলাফল (বোর্ড)")
        context['post']=post
    if navelement_head=="অনার্স" and heading=="ভর্তি বিজ্ঞপ্তি" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
    if navelement_head=="অনার্স" and heading=="ভর্তি আবেদন" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="ভর্তি আবেদন")
        context['post']=post
    if navelement_head=="অনার্স" and heading=="পরীক্ষার নোটিশ" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="পরীক্ষার নোটিশ")
        context['post']=post
    if navelement_head=="অনার্স" and heading=="ভর্তি আবেদন" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="ভর্তি আবেদন")
        context['post']=post
    if navelement_head=="অনার্স" and heading=="পরীক্ষার ফর্ম পূরণ" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="পরীক্ষার ফর্ম পূরণ")
        context['post']=post
    if navelement_head=="অনার্স" and heading=="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)")
        context['post']=post
        print(post)
    if navelement_head=="মাস্টার্স" and heading=="ভর্তি বিজ্ঞপ্তি" :
        post=Post.objects.filter(category__name="মাস্টার্স",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
    if navelement_head=="মাস্টার্স" and heading=="ভর্তি আবেদন" :
        post=Post.objects.filter(category__name="মাস্টার্স",tag__name="ভর্তি আবেদন")
        context['post']=post
    if navelement_head=="মাস্টার্স" and heading=="পরীক্ষার নোটিশ" :
        post=Post.objects.filter(category__name="মাস্টার্স",tag__name="পরীক্ষার নোটিশ")
        context['post']=post
    if navelement_head=="মাস্টার্স" and heading=="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)" :
        post=Post.objects.filter(category__name="মাস্টার্স",tag__name="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)")
        context['post']=post
    if navelement_head=="ডিগ্রি (পাশ)" and heading=="ভর্তি বিজ্ঞপ্তি" :
        post=Post.objects.filter(category__name="ডিগ্রি (পাশ)",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
    if navelement_head=="ডিগ্রি (পাশ)" and heading=="ভর্তি আবেদন" :
        post=Post.objects.filter(category__name="ডিগ্রি (পাশ)",tag__name="ভর্তি আবেদন")
        context['post']=post
    if navelement_head=="ডিগ্রি (পাশ)" and heading=="পরীক্ষার নোটিশ" :
        post=Post.objects.filter(category__name="ডিগ্রি (পাশ)",tag__name="পরীক্ষার নোটিশ")
        context['post']=post
    if navelement_head=="ডিগ্রি (পাশ)" and heading=="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)" :
        post=Post.objects.filter(category__name="ডিগ্রি (পাশ)",tag__name="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)")
        context['post']=post
    
        
    if heading =='অধ্যক্ষ':
        context['teacher'] = principal

    
    if heading =='উপাধ্যক্ষ':
        context['teacher'] = vice_principal

    if heading =='একাডেমিক কাউন্সিল':
        context['teachers'] = academic_council
    
    if heading =='শিক্ষকবৃন্দ':
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
    
    
    if(page.type=='1' or navitem_name=='অনলাইন ক্লাসসমুহ'):
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
    notices=Post.objects.all().order_by('-id')
    principal=Teacher.objects.filter(position=1, release_date=None,is_active=True).first()   
    vice_principal=Teacher.objects.filter(position=2, release_date=None,is_active=True).first()
    teachers=Teacher.objects.filter( release_date=None,is_active=True)
    academic_council=Teacher.objects.filter(Q(position=4)|Q(position=1)|Q(position=2), release_date=None,is_active=True)
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
    if heading =='অধ্যক্ষ':
        context['teacher'] = principal

    
    if heading =='উপাধ্যক্ষ':
        context['teacher'] = vice_principal

    if heading =='একাডেমিক কাউন্সিল':
        context['teachers'] = academic_council
    
    if heading =='শিক্ষকবৃন্দ':
        context['teachers'] = teachers
        
    if servicebox_title=="ভর্তি নির্দেশিকা" and heading=="এইচএসসি ভর্তি" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
        print(post)

    
    if servicebox_title=="ভর্তি নির্দেশিকা" and heading=="অনার্স ভর্তি" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
    if servicebox_title=="ভর্তি নির্দেশিকা" and heading=="মাস্টার্স ভর্তি" :
        post=Post.objects.filter(category__name="মাস্টার্স",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
    if servicebox_title=="ভর্তি নির্দেশিকা" and heading=="ডিগ্রি (পাশ) ভর্তি" :
        post=Post.objects.filter(category__name="ডিগ্রি (পাশ)",tag__name="ভর্তি বিজ্ঞপ্তি")
        context['post']=post
    if servicebox_title=="পরীক্ষাসমূহ" and heading=="বোর্ড পরীক্ষা (এইচএসচসি) " :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ফলাফল (বোর্ড)")
        context['post']=post
    if servicebox_title=="পরীক্ষাসমূহ" and heading=="অভ্যন্তরীণ পরীক্ষা( এইচএসসি)" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="অভ্যন্তরীণ পরীক্ষা")
        context['post']=post
    if servicebox_title=="পরীক্ষাসমূহ" and heading=="ডিগ্রি ও অন্যান্য পরীক্ষা" :
        post=Post.objects.filter(category__name="ডিগ্রি (পাশ)",tag__name="ডিগ্রি (পাশ) পরীক্ষা")
        context['post']=post
    if servicebox_title=="পরীক্ষাসমূহ" and heading=="পরীক্ষাসমূহ (জাতীয় বিশ্ববিদ্যালয়ের অধীন)" :
        post=Post.objects.filter(category__name="জাতীয় বিশ্ববিদ্যালয়",tag__name="জাতীয় বিশ্ববিদ্যালয় পরীক্ষা")
        context['post']=post
    if servicebox_title=="পরীক্ষাসমূহ" and heading=="পরীক্ষাসমূহ (জাতীয় বিশ্ববিদ্যালয়ের অধীন)" :
        post=Post.objects.filter(category__name="জাতীয় বিশ্ববিদ্যালয়",tag__name="জাতীয় বিশ্ববিদ্যালয় পরীক্ষা")
        context['post']=post
    
    if servicebox_title=="ফলাফলসমূহ" and heading=="বোর্ড পরীক্ষার ফলাফল" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ফলাফল (বোর্ড)")
        context['post']=post
    if servicebox_title=="ফলাফলসমূহ" and heading=="অভ্যন্তরীণ ফলাফল( এইচএসসি)" :
        post=Post.objects.filter(category__name="এইচএসসি",tag__name="ফলাফল (অভ্যন্তরীণ)")
        context['post']=post
    if servicebox_title=="ফলাফলসমূহ" and heading=="জাতীয় বিশ্ববিদ্যালয়ের ফলাফল" :
        post=Post.objects.filter(category__name="জাতীয় বিশ্ববিদ্যালয়",tag__name="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)")
        context['post']=post
    if servicebox_title=="ফলাফলসমূহ" and heading=="অভ্যন্তরীণ ফলাফল( অনার্স)" :
        post=Post.objects.filter(category__name="জাতীয় বিশ্ববিদ্যালয়",tag__name="ফলাফল (জাতীয় বিশ্ববিদ্যালয়)")
        context['post']=post
    
    if servicebox_title=="অনার্স" and heading=="পরীক্ষার নোটিশ" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="পরীক্ষার নোটিশ")
        context['post']=post
    if servicebox_title=="অনার্স" and heading=="ভর্তি আবেদন" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="ভর্তি আবেদন")
        context['post']=post
    if servicebox_title=="অনার্স" and heading=="পরীক্ষার ফর্ম পূরণ" :
        post=Post.objects.filter(category__name="অনার্স",tag__name="পরীক্ষার ফর্ম পূরণ")
        context['post']=post
    if servicebox_title=="অনলাইন ক্লাসসমূহ":
        navitem=NavItem.objects.filter(name='অনলাইন ক্লাসসমুহ').first()
        context['navitem']=navitem


    if(page.type=='1'):
        return render(request,'postview/showpage.html',context=context)
    elif(page.type=='2'):
        return render(request,page.template.directory+'/'+page.template.name,context=context)
    else:
        return redirect(page.link)
