from coms.models import PagesContent, Menu
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    list_display = ('name','link','content')
    
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_name')

admin.site.register(PagesContent, PageAdmin)
admin.site.register(Menu, MenuAdmin)