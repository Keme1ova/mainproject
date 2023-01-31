from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class OrderCreate(generic.CreateView):
    template_name = 'book.html'
    form_class = forms.Form_notes
    queryset = models.Order.objects.all()
    success_url = '/order/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(OrderCreate, self).form_valid(form=form)