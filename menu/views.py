from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import MenuForm
from .models import Menu
from .forms import FindForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#食品の一覧ページ、5件ごとのページネーションで表示のみ

def menu_index(request, num=1):
    data = Menu.objects.all()
    page = Paginator(data, 5)
    params = {
        'title' : 'Menu',
        'message': '',
        'data' : page.get_page(num),
    }
        
    return render(request, 'menu/menu_index.html', params)

#新しくオブジェクトを作成する専用ページ、追加後は一覧ページへ移行する

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

#既にあるオブジェクトを編集する専用ページ、編集後は/findへ移行する

def edit(request, num):

    obj = Menu.objects.get(id=num)

    if (request.method == 'POST'):
        menu = MenuForm(request.POST, instance=obj)
        menu.save()
        return redirect(to='/menu/find')

    params = {
        'title': 'Menu',
        'id': num,
        'form': MenuForm(instance=obj),
    }
    return render(request, 'menu/edit.html', params)

#既にあるオブジェクトを削除する専用ページ、編集後は/findへ移行する

def delete(request, num):
   
    menu = Menu.objects.get(id=num)

    if (request.method == 'POST'):
        menu.delete()
        return redirect(to='/menu/find')

    params = {
        'title': 'Menu',
        'id': num,
        'obj': menu,
    }

    return render(request, 'menu/delete.html', params)

#オブジェクトを検索する専用ページ、fav_trueにお気に入り登録したオブジェクト同士を合算させる

def find(request):

    template_name = 'find.html'

    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Menu.objects.filter(name__icontains = find)
        msg = 'Result: ' + str(data.count())

    else:
        msg = 'search words...'
        form = FindForm()
        data = Menu.objects.all()

    fav_true = Menu.objects.filter(favorite = True)

    callist = []
    for itemcal in fav_true:
        callist.append(itemcal.calorie)
    callist_sum = sum(callist)

    prolist = []
    for itempro in fav_true:
        prolist.append(itempro.protein)
    prolist_sum = sum(prolist)

    fatlist = []
    for itemfat in fav_true:
        fatlist.append(itemfat.fat)
    fatlist_sum = sum(fatlist)

    carlist = []
    for itemcar in fav_true:
        carlist.append(itemcar.carbohydrates)
    carlist_sum = sum(carlist)

    dielist = []
    for itemdie in fav_true:
        dielist.append(itemdie.dietary_fiber)
    dielist_sum = sum(dielist)

    totallist = {'cal':callist_sum, 'pro':prolist_sum, 'fat':fatlist_sum, 'car':carlist_sum, 'die':dielist_sum}

    params = {
        'title': 'Menu',
        'message': msg,
        'form': form,
        'data': data,
        'fav' : totallist,
    }
    
    return render(request, 'menu/find.html', params)

#お気に入り登録/解除したオブジェクトをsaveする

def favorite(request,num):

    menu = Menu.objects.get(id=num)

    if (menu.favorite == True):
        menu.favorite = False
        menu.save()
        return redirect(to='find')

    else
        menu.favorite = True
        menu.save()
        return redirect(to ='find')
        
    params = {
        'id': num,
    }

