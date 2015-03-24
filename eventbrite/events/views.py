from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import requests

from django.views.generic import FormView, TemplateView
from .forms import CategorySelectForm

EVENT_SEARCH_API = 'https://www.eventbriteapi.com/v3/events/search/?token=BKKRDKVUVRC5WG4HAVLT'


class CategorySelectView(FormView):
    """
        This view provides user a Category List page where they can select top 3 interested categories.
        After user submit the form, it will redirect the user to the event_list page based on their category selection
    """

    template_name = 'events/category_list.html'
    form_class = CategorySelectForm

    def form_valid(self, form):
        self.selected_categories = form.cleaned_data['category']
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        category_para = ",".join(str(category.cid) for category in self.selected_categories)
        event_list_url = reverse('event-list')
        url = event_list_url + "?categories=%s" % category_para
        return url


class EventListView(TemplateView):
    """
        This view get event information from Eventbrite API and display the list to the user
    """
    template_name = 'events/event_list.html'

    def get_list(self, page=1, categories=""):
        resp_json = None
        request_url = EVENT_SEARCH_API + "&page=%s&categories=%s" % (page, categories)
        resp = requests.get(request_url)
        if resp.status_code == 200:
            resp_json = resp.json()
        return resp_json

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        categories = self.request.GET.get('categories', "")
        repo_json = self.get_list(page=page, categories=categories)
        if repo_json:
            pagination = repo_json['pagination']
            if pagination['page_number'] < pagination['page_size']:
                context['next_page'] = pagination['page_number'] + 1
            if pagination['page_number'] > 1:
                context['previous_page'] = pagination['page_number'] - 1
            context['categories'] = categories
            context['event_list'] = repo_json['events']
        return context