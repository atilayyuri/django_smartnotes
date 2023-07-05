from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NotesForm


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"
    login_url = '/login'

class NotesCreateView(CreateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    #extra_context = {'user': Notes.objects.all()}
    # if the user tries to access the list but not logged
    # in than they will be directed to admin page
    login_url = "/login"

    # now end point is requiring  user authentication
    # and uses the user of that request
    def get_queryset(self):
        return self.request.user.notes.all()


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
    login_url = 'login'


# def detail(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist')
#     return render(request, 'notes/notes_detail.html', {'note':note})
