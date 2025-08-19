from .models import Post
from blog.models import Category,Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from account.models import UserModel

def posts(request):
        allposts=Post.objects.all().order_by('-id')

        d = timezone.now() - timedelta(days=45)
        post=Post.objects.all()
        latest_posts=Post.objects.all().order_by('-id')[:7]
        popular_posts = Post.objects.filter(date_created__gte=d, views__gt=0).order_by('views')[:5]
        users=UserModel.objects.all()
        post=Post.objects.all().order_by('-id')[:8]
        categories=Category.objects.all()
        tags=Tag.objects.all()

        post=Post.objects.order_by('date_created')
        page = request.GET.get('page', 1)
        paginator = Paginator(post, 5)
        try:
         post = paginator.page(page)
        except PageNotAnInteger:
         post = paginator.page(1)
        except EmptyPage:
         post = paginator.page(paginator.num_pages)
        return {
        'allposts': allposts,
          'post': post,
          'users':users,
          'popular_posts':popular_posts,
          'latest_posts':latest_posts,
          'categories':categories,
          'tags':tags
    }