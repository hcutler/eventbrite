from django.conf.urls import patterns, url
from .views import CategorySelectView

urlpatterns = patterns('',
    url(r'^$', CategorySelectView.as_view(), name='category-list')
)