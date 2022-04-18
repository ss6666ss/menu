from django.shortcuts import render
from django.http import HttpResponse
from .forms import MenuForm
from .models import Menu

def index(request):
    data = Menu.objects.all()
    params = {
        'title' : 'Menu',
        'message' : 'all menus',
        'form' : MenuForm(),
        'data' : [],

    }
    if (request.method == 'POST'):
        num=request.POST['id']
        item = Menu.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Menu.objects.all()
        
    return render(request, 'menu/index.html', params)

