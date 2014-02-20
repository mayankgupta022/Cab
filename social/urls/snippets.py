from django.conf.urls.defaults import *
from social.views.snippets import *
from social.models import Snippet

urlpatterns = patterns('',
						url(r'^$',
							SnippetListView.as_view(),
							name='cab_snippet_list'),
						url(r'^(?P<pk>\d+)/$',
							SnippetDetailView.as_view(),
							name='cab_snippet_detail'),
)