from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import MenuForm
from .models import Menu

def index(request):
    data = Menu.objects.all()
    params = {
        'title' : 'Menu',
        'data' : data,

    }
        
    return render(request, 'menu/index.html', params)

def create(request):
    if (request.method == 'POST'):
       obj = Menu()
       menu = MenuForm(request.POST, instance=obj)
       menu.save()
       return redirect(to='/menu')
    params = {
        'title' : 'Menu',
        'form' : MenuForm(),
     }
    return render(request, "menu/create.html", params)

def edit(request, num):
    obj = Menu.objects.get(id=num)
    if (request.method == 'POST'):
        menu = MenuForm(request.POST, instance=obj)
        menu.save()
        return redirect(to='/menu')
    params = {
        'title': 'Menu',
        'id': num,
        'form': MenuForm(instance=obj),
    }
    return render(request, 'menu/edit.html', params)
    