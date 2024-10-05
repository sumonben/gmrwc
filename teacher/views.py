from django.shortcuts import redirect, render
from frontpage.models import NavItem,Institute,Carousel
from .models import Teacher
from django.db.models import Count,Q

# Create your views here.
def teacher(request):
    return render("teacher/teacher_details.html")

def teacherList(request, content_name,head,type,heading):
    carousels = Carousel.objects.all().order_by('cid')
    institute=Institute.objects.first()
    navitems=NavItem.objects.all().order_by('serial')
    principal=Teacher.objects.filter(position__serial=1, release_date=None,is_active=True).first()   
    vice_principal=Teacher.objects.filter(position__serial=2, release_date=None,is_active=True).first()
    academic_council=Teacher.objects.filter(Q(position__serial=4)|Q(position__serial=1)|Q(position__serial=2), release_date=None,is_active=True).order_by('designation__serial','position__serial')
    print(vice_principal)
    context = {
        'carousels': carousels,
        'navitems':navitems,
        'heading':heading,
        'principal':principal,
        'institute':institute,
        'vice_principal':vice_principal,
        'academic_council':academic_council,
        }
    if heading == 'vacantpost':
        teachers=Teacher.objects.filter(~Q(position__serial=1),~Q(position__serial=2),release_date=None,is_active=True).order_by('t_department__serial','designation__serial','position__serial')
        context['teachers']=teachers
   
    
    return render(request,"teacher/teacher_vacant_post.html",context=context)