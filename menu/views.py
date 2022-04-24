from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import MenuForm
from .models import Menu
from .forms import FindForm
from django.core.paginator import Paginator

def index(request, num=1):
    data = Menu.objects.all()
    page = Paginator(data, 3)
    params = {
        'title' : 'Menu',
        'message': '',
        'data' : page.get_page(num),

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

def delete(request, num):
    menu = Menu.objects.get(id=num)
    if (request.method == 'POST'):
        menu.delete()
        return redirect(to='/menu')
    params = {
        'title': 'Menu',
        'id': num,
        'obj': menu,
    }
    return render(request, 'menu/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Menu.objects.filter(name__iexact=find)
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Menu.objects.all()
    params = {
        'title': 'Menu',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'menu/find.html', params)
