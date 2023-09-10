from django.contrib import admin
from myapp.models import member , postdata

# Register your models here.

class D_member(admin.ModelAdmin):
    list_display = ['id', 'phone' ,  'user']

class D_post(admin.ModelAdmin):
    list_display = ['id','description' , 'datetime' , 'user']

admin.site.register(member ,D_member)
admin.site.register(postdata, D_post)