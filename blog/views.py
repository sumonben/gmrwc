from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    MonthArchiveView
)
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timedelta
from django.utils import timezone
from itertools import count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from account.models import UserModel
from .models import Post,Tag,Category,Profile,CommentGuest,Comment,Like,YoutubeVideo
from django.db.models import Count
from .forms import PostCreateForm,CommentGuestForm,CommentForm
import datetime
# Create your views here.
def blog_index(request):
   # if request.user.is_authenticated:
        allpost=Post.objects.all().select_related('author').order_by('-id')

        d = timezone.now() - timedelta(days=15)
        post=Post.objects.all().select_related('author')
        latest_posts=Post.objects.all().select_related('author').order_by('-id')[:7]
        popular_posts = Post.objects.filter(date_created__gte=d, views__gt=0).order_by('-views')[:5]
        users=UserModel.objects.all()
        post=Post.objects.all().select_related('author').order_by('-id')[:8]
        categories=Category.objects.all()
        tags=Tag.objects.all()
        videos=YoutubeVideo.objects.all().order_by("-id")[:5] 
        page = request.GET.get('page', 1)
        paginator = Paginator(post, 3)
        try:
         post = paginator.page(page)
        except PageNotAnInteger:
         post = paginator.page(1)
        except EmptyPage:
         post = paginator.page(paginator.num_pages)
        context = {
          'allpost': allpost,
          'post': post,
          'users':users,
          'popular_posts':popular_posts,
          'latest_posts':latest_posts,
          'categories':categories,
          'tags':tags,
          'videos':videos
     }  
        return render(request,'blog/blog_index.html',context=context)
    #else:
        return redirect('login')  
    

    
class PostView(DetailView):
    model = Post
    template_name = "blog/singlepost.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        

        d = timezone.now() - timedelta(days=30)
        singlepost=get_object_or_404(Post, pk=pk)
        singlepost.views+=1
        singlepost.save()
        allpost=Post.objects.all().select_related('author').order_by('-id')
        videos=YoutubeVideo.objects.all().order_by("-id")[:5] 
        post=Post.objects.all().select_related('author').order_by('-id')[:10]
        related_posts = Post.objects.filter(categories__in=singlepost.categories.all()).distinct()
        categories=Category.objects.all()
        tags=Tag.objects.all()
        popular_posts = Post.objects.filter(date_created__gte=d, views__gt=0).order_by('-views')[:5]
        form = CommentGuestForm()
        comments = singlepost.commentguest.all()
        allcomments=CommentGuest.objects.all().order_by("-id")[:10]
        liked = False
        if singlepost.likes.filter(id=self.request.user.id).exists():
            liked = True
            print(liked)
            # next -> get posts with id greater than the current post id, then get the first instance 'next post'
     # previous -> get posts with id less than the current post id, then get the first instance 'previous post'
        context = {
          'allpost':allpost,
          'singlepost':singlepost,
          'post':post,
          'next': related_posts.filter(id__gt=singlepost.id).order_by('id').first(), 
          'previous': related_posts.filter(id__lt=singlepost.id).order_by('-id').first(),
          'related_posts':related_posts,
          'popular_posts':popular_posts,
          'categories':categories,
          'tags':tags,
          'form': form,
          'comments':comments,
          'allcomments':allcomments,
          'number_of_likes':singlepost.number_of_likes(),
          'post_is_liked':liked,
          'videos':videos
         }
        return context
    
    def post(self, request, *args, **kwargs):
        d = timezone.now() - timedelta(days=8)
        form = CommentGuestForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.commentguest.all()
        allcomments=CommentGuest.objects.all().order_by("-id")[:10]
        videos=YoutubeVideo.objects.all().order_by("-id")[:5] 
        related_posts = Post.objects.filter(categories__in=post.categories.all()).distinct()
        categories=Category.objects.all()
        tags=Tag.objects.all()
        popular_posts = Post.objects.filter(date_created__gte=d, views__gt=0).order_by('-views')[:5]
        context['singlepost'] = post
        context['related_posts'] = related_posts
        context['categories'] = categories
        context['tags'] = tags
        context['popular_posts'] = popular_posts
        context['comments'] = comments
        context['form'] = form
        context['form'] = form
        context['allcomments'] = allcomments
        context['videos'] = videos


        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
           
            comment = CommentGuest.objects.create(
                name=name, email=email, content=content, post=post,date_posted=datetime.datetime.now()
            )

            form = CommentGuestForm()
            context['form'] = form
            return self.render_to_response(context=context)
        context['login'] = form
        return self.render_to_response(context=context)
    

def BlogPostLike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    ip_address = request.META.get('REMOTE_ADDR')
    print("IP_Address",ip_address)
    context={}
    if ip_address:
            try:
                Like.objects.create(post=post, ip_address=ip_address)
                post.like+=1
                post.save()
            except IntegrityError:
                context['liked']=True

    return HttpResponseRedirect(reverse('singlepost', args=[str(pk)]),context)    
    



def singlePost(request, pk):
    d = timezone.now() - timedelta(days=8)
    singlepost=get_object_or_404(Post, pk=pk)
    post=Post.objects.all().select_related('author').order_by('-id')[:7]
    related_posts = Post.objects.filter(categories__in=singlepost.categories.all()).distinct()
    categories=Category.objects.all()
    tags=Tag.objects.all()
    popular_posts = Post.objects.filter(date_created__gte=d, views__gt=0).order_by('-views')[:5]
    form = CommentGuestForm()
    comments = post.comment_set.all()
    allcomments=CommentGuest.objects.all().order_by("-id")[:10]
    videos=YoutubeVideo.objects.all().order_by("-id")[:5] 

     # next -> get posts with id greater than the current post id, then get the first instance 'next post'
     # previous -> get posts with id less than the current post id, then get the first instance 'previous post'
    context = {
          'singlepost':singlepost,
          'post': post,
          'next': related_posts.filter(id__gt=singlepost.id).order_by('id').first(), 
          'previous': related_posts.filter(id__lt=singlepost.id).order_by('-id').first(),
          'related_posts':related_posts,
          'popular_posts':popular_posts,
          'categories':categories,
          'tags':tags,
          'form': form,
          'comments':comments,
          'allcomments':allcomments,
          'videos':videos
     }  
    return render(request,'blog/singlepost.html',context=context)


def creatPost(request): 
 if request.user.is_authenticated:
    user = request.user
    form = PostCreateForm()
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            user = Profile.objects.filter(user=request.user).first()
            categories=form.cleaned_data['categories']
            tags=form.cleaned_data['tags']

            print(categories)
            new_post = form.save(commit=False)
            print(request.user)

            new_post.author = user
            new_post.save()
            new_post.categories.set(categories)
            new_post.tags.set(tags)
            for cat in categories:
                print(cat)
                #new_post.categories.add(cat)
            new_post.save()
            #form.save_m2m()
        else:
            return HttpResponse(form.errors)
    return render(request, 'blog/postcreate.html', {'form': form})
 return redirect('login')


def showMultiple(request, type, id):
    d = timezone.now() - timedelta(days=100)
    post=Post.objects.all().select_related('author').order_by('-id')[:7]
    categories=Category.objects.all()
    tags=Tag.objects.all()
    popular_posts = Post.objects.filter(date_created__gte=d, views__gt=0).order_by('-views')[:5]    
    form = CommentGuestForm()
    comments=CommentGuest.objects.all().order_by("-id")
    videos=YoutubeVideo.objects.all().order_by("-id")[:5] 

    if type in 'category':
        allpost = Post.objects.filter(categories__id=id).order_by('-id').distinct()
        name=Category.objects.filter(id=id).first()
    elif type in 'tag':
        allpost = Post.objects.filter(tags__id=id).order_by('-id').distinct()
        name=Tag.objects.filter(id=id).first()
    page = request.GET.get('page', 1)
    paginator = Paginator(allpost, 6)
    try:
         allpost = paginator.page(page)
    except PageNotAnInteger:
         allpost = paginator.page(1)
    except EmptyPage:
         allpost = paginator.page(paginator.num_pages)    

    
    context = {
          'allpost':allpost,
          'post': post,
          'popular_posts':popular_posts,
          'categories':categories,
          'tags':tags,
          'type':type,
          'name':name,
          'comments':comments,
          'videos':videos


     }
    return render(request,'blog/showmultiple.html',context=context)
        


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "date_created"
    allow_future = True
    
    
    