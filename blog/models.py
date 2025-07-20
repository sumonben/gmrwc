from datetime import date
from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
import random
import string

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()
    
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    name_en = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    name_en = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class PlaceHolder(models.Model):
    serial=models.IntegerField(default=0)
    name = models.CharField(max_length=50, unique=True)
    name_en = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name+":"+self.name_en
    
class Post(models.Model):
    class Meta:
        ordering = ["publish_date"]
    
    serial=models.IntegerField(default=0)
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, allow_unicode=True, unique=True)
    body=RichTextUploadingField(blank=True,null=True)
    body_en=RichTextUploadingField(blank=True,null=True)    
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    place_holder=models.ManyToManyField(PlaceHolder, blank=True,null=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='blog_posts')
    image=models.ImageField(upload_to='media/news',blank=True,null=True)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.author) + "-" + str(self.pk)
            self.save()
    def publish(self):
        self.published_date = date.today()
        self.published=True
        self.save()
    def get_absolute_url(self):
        return reverse("singlepost", args=[str(self.id)])
    
    def get_related_posts_by_tags(self):
        return Post.objects.filter(tags__in=self.tags.all())
    def number_of_likes(self):
        return self.likes.all().count()
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True,null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = RichTextField()
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return '{} - {}'.format(self.author, self.date_posted)

class CommentGuest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = RichTextField()
    post = models.ForeignKey(Post, related_name='commentsguest', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return 'Comment by {}-{}'.format(self.name,self.email)