from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Post
from django.contrib.auth import logout
from django.core.paginator import Paginator

def index(request):
    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Listing'
    all_post = Post.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'goods/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Add'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['form'] = PostForm()
            return render(request, 'goods/create.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
        # =======================

    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/goods')


def details(request, post_id):
    data = dict()
    data['title'] = 'View '
    data['post'] = Post.objects.get(id=post_id)
    return render(request, 'goods/details.html', context=data)


def edit(request, post_id):
    data = dict()
    data['title'] = 'Edit '
    post = Post.objects.get(id=post_id)
    # del ... ?
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['form'] = PostForm2(instance=post)
            data['post'] = post
            return render(request, 'goods/edit.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        # print('==', form2)
        if form2.is_valid():
            # post.photo = form2.cleaned_data['photo']
            post.name = form2.cleaned_data['name']
            post.description = form2.cleaned_data['description']
            post.type = form2.cleaned_data['type']
            post.status = form2.cleaned_data['status']
            post.location = form2.cleaned_data['location']
            post.beds = form2.cleaned_data['beds']
            post.baths = form2.cleaned_data['baths']
            post.floors = form2.cleaned_data['floors']

            post.metro = form2.cleaned_data['metro']
            post.area = form2.cleaned_data['area']
            post.size = form2.cleaned_data['size']
            post.photoURL = form2.cleaned_data['photoURL']
            post.videoURL = form2.cleaned_data['videoURL']

            post.address = form2.cleaned_data['address']
            post.city = form2.cleaned_data['city']
            post.country = form2.cleaned_data['country']
            # fields = ('name', 'description', 'type', 'status', 'location', 'beds', 'baths', 'floors', 'metro', 'area',
            #           'size', 'photoURL', 'videoURL', 'address', 'city', 'country')
            post.save()
        return redirect('/goods')



def delete(request, post_id):
    data = dict()
    data['title'] = 'Delete artwork'
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin' or request.user.username == 'admin1':
            data['post'] = post
            return render(request, 'goods/delete.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
    elif request.method == 'POST':
        post.delete()
        return redirect('/goods')
