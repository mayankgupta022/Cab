from django.conf.urls.defaults import *
from social.views.languages import *
from social.models import Language

urlpatterns = patterns('',
		url(r'^$',
			LanguageListView.as_view(),
			name='cab_language_list'),
		# url(r'^(?P<slug>[-\w]+)/$',
		# 	LanguageDetailView.as_view(),
		# 	name='cab_language_detail'),
)