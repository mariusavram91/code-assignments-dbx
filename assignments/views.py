from django.views import generic
from django.shortcuts import get_object_or_404
from assignments.models import Assignment


class IndexView(generic.ListView):
    model = Assignment
    template_name = "index.html"
    context_object_name = "assignments"
    queryset = Assignment.objects.all()


class ShowView(generic.DetailView):
    model = Assignment
    template_name = "show.html"
    context_object_name = "assignment"

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return get_object_or_404(Assignment, pk=pk)


class NewView(generic.CreateView):
    model = Assignment

    fields = ['candidate', 'email', 'position']

    template_name = "new.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)

        context['positions'] = ['Python Developer', 'Full Stack Developer']

        return context
