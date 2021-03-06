from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import api.views

urlpatterns = [
	url(r'^categories/(?P<categoryId>[0-9]+)$', api.views.CategoryImageList.as_view()),
    	url(r'^categories/$', api.views.CategoriesList.as_view()),
    	url(r'^feed/$', api.views.FeedActivityList.as_view()),
    	url(r'^subscribe/$', api.views.Subscribe.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
