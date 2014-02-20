from social.models import *
from django.contrib import admin

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','lslug','language_code','mime_type')
    
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language','author','pub_date','updated_date')

admin.site.register(Language, LanguageAdmin)
admin.site.register(Snippet, SnippetAdmin)