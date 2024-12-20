from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Carousel,Category,Tag,NavItem,NavElement,Page,ServiceBox,Notice,Post,Template,Institute
# Register your models here.
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple


    # ...

    
@admin.register(Carousel)
class CaroselAdmin(admin.ModelAdmin):
    list_display=['cid', 'cname','ctext','cimage']

'''@admin.register(Teacher)
class ProfileAdmin(admin.ModelAdmin):
    model = Teacher
@admin.register(Department)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'serial','name','code',]
    list_filter=[  'name','code',]

@admin.register(Branch)
class UserAdmin(admin.ModelAdmin):
    list_display=[   'serial','name','code',]
    list_filter=[  'name','code',]
'''

@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'name','name_en']
    filter_fields=[  'name',]


@admin.register(Tag)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'name','name_en']
    filter_fields=[  'name',]

@admin.register(Template)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'name','directory']
    filter_fields=[  'name',]
    
@admin.register(Page)
class UserAdmin(admin.ModelAdmin):
    search_fields=[  'heading','heading_en']
    list_display=[   'serial','heading','heading_en','parent_nav_link','link','template']
    filter_fields=[  'title']
    list_filter=[  'category']
    filter_horizontal = ['category','tag']
    list_display_links = ['serial','heading']


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display=[   'serial','heading','heading_en','title','body']
    filter_fields=[  'title',]
    filter_horizontal = ['category','tag']

@admin.register(Notice)
class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display=[  'title','body']
    filter_fields=[  'title',] 
    
@admin.register(NavElement)
class NavElementAdmin(admin.ModelAdmin):
    filter_horizontal = ['page',]
    list_display=[   'serial','head','head_en', 'Related_pages']
    list_display_links = ['head','serial']
    search_fields=[  'head',]
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'your_sortedm2m_field_name':
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super(NavElementAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
@admin.register(NavItem)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ['navelement',]
    list_display=[ 'serial','name','name_en','Child_Element_link']
    search_fields=[  'name',]
    list_display_links = ['serial','name']
    
@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display=[   'serial','title','eiin_no']
    search_fields=[  'title','eiin_no']
    list_display_links = ['serial','title']


@admin.register(ServiceBox)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ['element',]
    list_display=[   'serial','title','title_en','Related_pages']
    search_fields=[  'title',]
    list_display_links = ['serial','title']
