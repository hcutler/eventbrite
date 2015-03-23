from django.views.generic import FormView
from .forms import CategorySelectForm


class CategorySelectView(FormView):
    template_name = 'events/category_list.html'
    form_class = CategorySelectForm