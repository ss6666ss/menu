from django.shortcuts import render
from django.http import HttpResponse
from .forms import MenuForm

def index(request):
    data = Menu.objects.all()
    params = {
        'title' : 'Menu',
        'message' : 'all menus',
        'data' : data,
    }
        
    return render(request, 'menu/index.html', params)

