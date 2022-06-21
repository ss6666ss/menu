from django.shortcuts import render
from django.shortcuts import reirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.pagintor import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Message,Friend,Group,Good
from .forms import GroupCheckForm,GroupSelectForm,FriendsForm,CreateGroupForm,PostForm

@login_required(login_url = '/admin/login/')
def index(request, page = 1):
    (public_user, public_group) = get_public()

    if request.method == 'POST':

        checkform = GroupCheckForm(request.user, request.POST)
        glist = []
        for item in request.POST.getlist('groups'):
            glist.append(item)
        
        messages = get_your_group_message(request.user, glist, page)
    
    else:
        checkform = GroupCheckForm(request.user)
        gps = Group.objects.filter(owner = request.user)
        glist = [public_group.title]
        for item in gps:
            glist.append(item.title)
        
        messages = get_your_group_message(request.user, glist, page)

    params = {
        'login_user' : request.user,
        'contents' : messages,
        'check_form' : checkform,
    }

    return render(request, 'sns/index.html', params)

@login_required(login_url = '/admin/login/')
def groups(request):
    friends = Friend.objects.filter(owner = request.user)

    if request.method == 'POST':
        if request.POST['mode'] == '__groups_form__':
            sel_group = request.POST['groups']
            gp = Group.objects.filter(owner = request.user).filter(title = sel_group).first()
            fds = friend.objects.filter(owner = request.user).filter(group = gp)
            print(Friend.objects.filter(owner = request.user))
            vlist = []

            for item in fds:
                vlist.append(item.user.username)
            
            groupsform = GroupSelectForm(request.user, request.POST)
            friendsform - FriendsForm(request.user, friends = friends, vals = vlist)

        if request.POST['mode'] == '__friends_form__':
            selgroup request.POST['group']
            group_obj = Group.objects.filter(title = sel_group).first()
            print(group_obj)
            sel_fds = request.POST.getlist('friends')
            sel_users = User.objects.filter(username__in = sel_fds)
            fds = Friend.objects.filter(owner = request.user).filter(user__in = sel_users)
            vlist = []

            for item in fds:
                item.group = group_objitem.save()
                vlist.append(item.user.username)
            
            messages.success(request, ' チェックされたFriendを ' + sel_group + ' に登録しました。 ')
            groupsform = GroupSelectForm(request.user, {'groups' : sel_group})
            friendsform = FriendsForm(request.user, friends = friends, vals = vlist)
    
    else:
        groupsform = GroupSelectForm(request.user)
        friendsform = FriendsForm(request.user, friends = friends, vals = [])
        sel_group = '-'

    createform = CreateGroupForm()
    params = {
        'login_user' : request.user,
        'groups_form' : groupsform,
        'friends_form' : friendsform,
        'create_form' : createform,
        'group' : sel_group,
    }

    return render(request, 'sns/groups.html', params)

@login_required(login_url = '/admin/login')
def add(request):
    add_name = request.GET['name']
    add_user = User.objects.filter(username = add_name).first()

    if add_user == request.user:
        messages.info(requet, "自分自身をFriendに追加することはできません。")
        
        return redirect(to = '/sns')

    (public_user, public_group) = get_public()
    frd_num = Friend.objects.filter(owner = request.user).filter(user = add_user).count()

    if frd_num > 0:
        messages.info(request, add_user.username + ' は既に追加されています。 ')

        return redirect(to = '/sns')

    frd = Friend()
    frd.owner = request.user
    frd.user = add_user
    frd.group = public_group
    frd.save()
    messages.success(request, add_user.username + ' を追加しました！ groupページに移動して、追加したFriendをメンバーに設定してください。')

    return redirect(to = '/sns')