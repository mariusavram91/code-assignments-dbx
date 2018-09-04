from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from dbx.services import Dropbox
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
        assignment = get_object_or_404(Assignment, pk=pk)

        dropbox = Dropbox()
        assignment.link = dropbox.get_file_link(assignment.dropbox_id)

        return assignment


class NewView(generic.CreateView):
    model = Assignment

    fields = ['candidate', 'email', 'position']

    template_name = "new.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)

        context['positions'] = ['Python Developer', 'Full Stack Developer',
                                'Frontend Developer', 'Software Engineer']

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        assignment = form.save()

        dropbox = Dropbox()
        assignment.dropbox_id = dropbox.upload_file(
            request.FILES['assignment_file'],
            request.POST['candidate']
        )
        assignment.save()

        return redirect(self.success_url)
