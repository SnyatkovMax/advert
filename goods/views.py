from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    data = dict()
    data['user'] = 'admin'
    all_posts = Post.objects.all()
    data['posts'] = all_posts

    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return render(request, 'home/index.html', context=data)


def create(request):
    data = dict()
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
        return redirect('/home/index.html')


def details(request, post_id):
    pass


def edit(request, post_id):
    pass


def delete(request, post_id):
    pass
