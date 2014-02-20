from django.conf.urls.defaults import *
from social.views import *
from social.models import Snippet

snippet_info = { 'queryset': Snippet.objects.all() }

urlpatterns = patterns('',
						url(r'^$',
							SnippetListView.as_view(),
							# dict(snippet_info, paginate_by=20),
							name='cab_snippet_list'),
						url(r'^(?P<pk>\d+)/$',
							SnippetDetailView.as_view(),
							name='cab_snippet_detail'),
)