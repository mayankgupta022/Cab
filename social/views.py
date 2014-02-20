# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from social.models import *

class SnippetDetailView(DetailView):

    model = Snippet
    object_id=Snippet.pk

    # def get_context_data(self, **kwargs):
    #     context = super(SnippetDetailView, self).get_context_data(**kwargs)
    #     return context


class SnippetListView(ListView):

    model = Snippet
    paginate_by=1

    # def get_context_data(self, **kwargs):
    #     context = super(SnippetListView, self).get_context_data(**kwargs)
    #     return context