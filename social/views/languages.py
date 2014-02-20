# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from social.models import Language, Snippet

# class LanguageDetailView(DetailView):

#     model=Language
#     paginate_by=20
#     template_name='social/language_detail.html'

#     def get_queryset(self):
#         self.language = Language.objects.get(lslug=self.kwargs['slug'])
#         return Snippet.objects.filter(language=self.language)

    # def get_context_data(self, **kwargs):
    #     context = super(LanguageDetailView, self).get_context_data(**kwargs)
    #     extra_context={ 'language': language }
    #     return extra_context

class LanguageListView(ListView):

    model = Language
    paginate_by=1

    # def get_context_data(self, **kwargs):
    #     context = super(LanguageListView, self).get_context_data(**kwargs)
    #     return context