from django.contrib import admin
from .models import *

class couresmodel(admin.ModelAdmin):
    list_display=['name','lang','price','img']

admin.site.register(cou,couresmodel)

class readmin(admin.ModelAdmin):
    list_display=['name','phone','date']

admin.site.register(re,readmin)

class signadmin(admin.ModelAdmin):
    list_display=['email','Password']

admin.site.register(sign,signadmin)