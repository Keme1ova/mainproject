from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic



class View_user_notes(generic.ListView):
    template_name = 'all.html'
    queryset = models.Model_notes_of_user.objects.all()

    def get_queryset(self):
        return models.Model_notes_of_user.objects.all()




class View_create_note(generic.CreateView):
    template_name = 'add.html'
    form_class = forms.Form_notes
    queryset = models.Model_notes_of_user.objects.all()
    success_url = '/notes/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(View_create_note, self).form_valid(form=form)



