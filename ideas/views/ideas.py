from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect
from ideas.models import Ideas
from ideas.forms.ideas_form import IdeasForm
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages



def base(request):
    return render(request, 'base.html')

class IdeaListView(ListView):
    model = Ideas
    template_name: str = 'ideas/list.html'
    context_object_name = 'ideas'
    permission_required = 'ideas.view_ideas'

    queryset =[]

class IdeaCreateView(CreateView):
    model = Ideas
    form_class = IdeasForm
    template_name = 'ideas/create.html'
    success_url = reverse_lazy('ideas:ideas_list')
    permission_required = 'ideas.add_ideas'

    def form_valid ( self , form ) :
        messages.success ( self.request , ' Registro creado con éxito ' )
        return super ( ) . form_valid ( form )
    

class IdeaUpdateView(UpdateView):
    model = Ideas
    form_class = IdeasForm
    template_name = 'ideas/update.html'
    success_url = reverse_lazy('ideas:ideas_list')
    permission_required = 'ideas.update_ideas'
    
    def form_valid ( self , form ) :
        messages.success ( self.request , ' Registro actualizado con éxito ' )
        return super ( ) . form_valid ( form )

class IdeaDeleteView( DeleteView):
    model = Ideas
    template_name = 'ideas/delete.html'
    success_url = reverse_lazy('ideas:ideas_list')
    context_object_name = 'ideas'
    permission_required = 'ideas.delete_ideas'
    

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Registro eliminado con éxito')
        return super().delete(*args, **kwargs)

class IdeaDetailView( DetailView):
    model = Ideas
    template_name = 'ideas/detail.html'
    context_object_name = 'ideas'
    permission_required = 'ideas.view_ideas'