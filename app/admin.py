from django.contrib import admin
from .models import Myform
# Register your models here.


class FormData(admin.ModelAdmin):
    list_display = ['id','acidity1','quantity1','acidity2','quantity2','acidity3','quantity3','total']


admin.site.register(Myform,FormData)
