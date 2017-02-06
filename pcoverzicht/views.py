from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from pcoverzicht.models import Computer, Software
from pcoverzicht.forms import ComputerForm
# Create your views here.


class ComputerListView(ListView):
    model = Computer
    template_name = 'pcoverzicht/computer_list.html'


class ComputerCreate(CreateView):
    model = Computer
    success_url = reverse_lazy('computer_list')
    # template_name = 'pcoverzicht/computer_form.html'
    fields = '__all__'


class ComputerUpdate(UpdateView):
    model = Computer
    success_url = reverse_lazy('computer_list')
    template_name = 'pcoverzicht/computer_update.html'
    fields = '__all__'


class ComputerDelete(DeleteView):
    model = Computer
    template_name = 'pcoverzicht/computer_confirm_delete.html'
    success_url = reverse_lazy('computer_list')


class SoftwareListView(ListView):
    model = Software


class SoftwareCreate(CreateView):
    model = Software
    success_url = reverse_lazy('software_list')
    template_name = 'pcoverzicht/software_form.html'
    fields = '__all__'


class SoftwareUpdate(UpdateView):
    model = Software
    success_url = reverse_lazy('software_list')
    template_name = 'pcoverzicht/software_update.html'
    fields = '__all__'


class SoftwareDelete(DeleteView):
    model = Software
    success_url = reverse_lazy('software_list')


class ComputerForm(FormView):
    template_name = 'pcoverzicht/computer_form2.html'
    form_class = ComputerForm
    succes_url = reverse_lazy('computer_list')

    def get_object(self, queryset=None):
        obj = Computer.objects.get(naam='SP4-2016-006')
        print(obj)
        return obj

    # def form_valid(self, form):
    #     obj = form.save()
    #     return HttpsResponseDirect('computerlist')


