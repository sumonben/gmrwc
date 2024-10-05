from import_export import resources,fields
from import_export.widgets import ManyToManyWidget
from .models import Student,StudentCategory
from django.forms import Field

class SpeciesResource(resources.ModelResource):
    student_category=fields.Field(widget=ManyToManyWidget(StudentCategory,field='student_category'), column_name='student_category')
    email = fields.Field(column_name='email')
    class Meta:
        model = Student
        fields =('email','student_category')
        export_order = fields