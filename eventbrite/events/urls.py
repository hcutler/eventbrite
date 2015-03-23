from django.conf.urls import patterns, url
from .views import CategorySelectView, EventListView

urlpatterns = patterns('',
    url(r'^$', CategorySelectView.as_view(), name='category-list'),
    url(r'^eventlist/', EventListView.as_view(), name='event-list')
)