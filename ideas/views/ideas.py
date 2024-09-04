
from django.shortcuts import render
from ideas.models import APIClient
from django.shortcuts import render, redirect
from ideas.forms.ideas_form import IdeasForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import requests
from django.contrib import messages

def list_ideas(request):
    client = APIClient('ideas')
    ideas = client.get_data()
    return render(request, 'ideas/list.html', {'ideas': ideas})


def create_idea(request):
    if request.method == 'POST':
        form = IdeasForm(request.POST, request.FILES)
        if form.is_valid():
            client = APIClient('ideas')
            try:
                response = client.insert_data(json_data=form.cleaned_data)
                messages.success(request, 'Idea creada con éxito.')
                return redirect('list')
            except requests.exceptions.HTTPError as e:
                messages.error(request, f'Error al crear la idea: {e}')
                print(f'Error al crear la idea: {e}')  # Depuración
            except Exception as e:
                messages.error(request, f'Error inesperado: {e}')
                print(f'Error inesperado: {e}')  # Depuración
    else:
        form = IdeasForm()
    return render(request, 'ideas/create.html', {'form': form})



def update_idea(request, pk):
    client = APIClient('ideas')
    idea = client.get_data(where_condition=f"id = {pk}")
    if not idea:
        return redirect('list')

    if request.method == 'POST':
        form = IdeasForm(request.POST, request.FILES)
        if form.is_valid():
            client.update_data(where_condition=f"id = {pk}", json_data=form.cleaned_data)
            messages.success(request, 'Idea actualizada con éxito.')
            return redirect('list')
    else:
        form = IdeasForm(initial=idea[0])

    return render(request, 'ideas/update.html', {'form': form})



def delete_idea(request, pk):
    client = APIClient('ideas')
    idea = client.get_data(where_condition=f"id = {pk}")
    if not idea:
        return redirect('list')

    if request.method == 'POST':
        client.delete_data(where_condition=f"id = {pk}")
        messages.success(request, 'Idea eliminada con éxito.')
        return redirect('list')

    return render(request, 'ideas/delete.html', {'idea': idea[0]})