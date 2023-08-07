from django.contrib import admin
from .models import careers,test
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class careersadmin(admin.ModelAdmin):
    
    fieldsets=[('title/date',{'fields':['career_title','career_published']}),('content',{'fields':['career_content']})]
    formfield_overrides={models.TextField:{'widget':TinyMCE()}}        
admin.site.register(careers,careersadmin)
admin.site.register(test)

