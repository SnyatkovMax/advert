from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth import logout


def create(request):
    data = dict()
    data['user'] = 'admin'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку!
        # =========================================
        if request.user.username == 'admin':
            data['form'] = PostForm()
            return render(request, 'home/add-property.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
        # =========================================
    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/home/index')



def details(request, post_id):
    pass


def edit(request, post_id):
    pass


def delete(request, post_id):
    pass
