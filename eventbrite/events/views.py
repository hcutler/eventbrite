import requests

from django.views.generic import FormView, TemplateView
from .forms import CategorySelectForm

EVENT_SEARCH_API = 'https://www.eventbriteapi.com/v3/events/search/?token=BKKRDKVUVRC5WG4HAVLT'

class CategorySelectView(FormView):
    template_name = 'events/category_list.html'
    form_class = CategorySelectForm


class EventListView(TemplateView):
    template_name = 'events/event_list.html'

    def get_list(self, page=1):
        resp_json = None
        request_url = EVENT_SEARCH_API + "&page=%s" % page
        resp = requests.get(request_url)
        if resp.status_code == 200:
            resp_json = resp.json()
        return resp_json

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        repo_json = self.get_list(page=page)
        pagination = repo_json['pagination']
        if pagination['page_number'] < pagination['page_size']:
            context['next_page'] = pagination['page_number'] + 1
        if pagination['page_number'] > 1:
            context['previous_page'] = pagination['page_number'] - 1
        event_list = repo_json['events']
        context['event_list'] = event_list
        return context