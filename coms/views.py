# Create your views here.
from django.shortcuts import render_to_response
from coms.models import PagesContent, Menu
from django.template import RequestContext

def writeup(request, name = 'home'):
    dictionary = {}
    dictionary['writeup']=PagesContent.objects.get(link=name)
    dictionary['menus']=PagesContent.objects.all()
    return render_to_response('content.htm',dictionary,context_instance=RequestContext(request))