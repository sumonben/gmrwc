from django.contrib import admin



from blog.models import Profile, Post, Tag,Category,Comment,CommentGuest,PlaceHolder,Like,YoutubeVideo
import random
import string
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
@admin.register(PlaceHolder)
class PlaceHolderAdmin(admin.ModelAdmin):
    model = PlaceHolder
@admin.register(YoutubeVideo)
class YoutubeVideoAdmin(admin.ModelAdmin):
    model = YoutubeVideo
    list_display = ('id',"serial","title",'embeded_link')
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    model = Like
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment

@admin.register(CommentGuest)
class CommentGuestAdmin(admin.ModelAdmin):
    model = CommentGuest 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    
    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True