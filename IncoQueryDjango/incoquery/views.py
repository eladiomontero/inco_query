from django.views.generic import ListView
from incoquery.models import IncoqueryQuery
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView

class ListQueryView(ListView):
    model = IncoqueryQuery
    template_name = 'query_list.html'

class CreateQueryView(CreateView):

    model = IncoqueryQuery
    template_name = 'edit_query.html'

    def get_success_url(self):
        return reverse('query-list')

    def get_context_data(self, **kwargs):

            context = super(CreateQueryView, self).get_context_data(**kwargs)
            context['action'] = reverse('query-new')

            return context

class UpdateQueryView(UpdateView):

    model = IncoqueryQuery
    template_name = 'edit_query.html'

    def get_success_url(self):
        return reverse('query-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateQueryView, self).get_context_data(**kwargs)
        context['action'] = reverse('query-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

