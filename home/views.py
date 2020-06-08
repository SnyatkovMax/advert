from django.shortcuts import render, redirect
from goods.models import Post
from django.core.paginator import Paginator



def index(request):

    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Listing'
    all_post = Post.objects.all()[::-1] # в обратном порядке
    data['posts'] = all_post
    paginator = Paginator(all_post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    # return render(request, 'home/index.html')
    return render(request, 'home/index.html', context=data)




def home_map(request):
    return render(request, 'home/home-map.html')
def home_property(request):
    return render(request, 'home/home-property.html')
def home_splash(request):
    return render(request, 'home/home-splash.html')


def agents(request):
    return render(request, 'home/agents.html')
def agent_profile(request):
    return render(request, 'home/agent-profile.html')
def agency_list(request):
    return render(request, 'home/agency-list.html')
def agency_profile(request):
    return render(request, 'home/agency-profile.html')

def service(request):
    return render(request, 'home/service.html')
def service_details(request):
    return render(request, 'home/service-details.html')



def page_about(request):
    return render(request, 'home/page-about.html')
def page_contact(request):
    return render(request, 'home/page-contact.html')
def page_faq(request):
    return render(request, 'home/page-faq.html')
def page_404(request):
    return render(request, 'home/page-404.html')


def blog(request):
    return render(request, 'home/blog.html')
def blog_sidebar_right(request):
    return render(request, 'home/blog-sidebar-right.html')
def blog_sidebar_left(request):
    return render(request, 'home/blog-sidebar-left.html')
def blog_single(request):
    return render(request, 'home/blog-single.html')


def user_profile(request):
    return render(request, 'accounts/user-profile.html')
def social_profile(request):
    return render(request, 'accounts/social-profile.html')
def my_properties(request):
    return render(request, 'home/my-properties.html')
def favourite_properties(request):
    return render(request, 'home/favourite-properties.html')
# def add_property(request):
#     return render(request, 'home/add-property.html')



def properties_grid(request):
    return render(request, 'home/properties-grid.html')

def properties_grid_split(request):

    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Listing'
    all_post = Post.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return render(request, 'home/properties-grid-split.html', context=data)

def properties_list(request):
    return render(request, 'home/properties-list.html')
def properties_list_split(request):
    return render(request, 'home/properties-list-split.html')
def property_single_gallery(request):
    return render(request, 'home/property-single-gallery.html')
def property_single_slider(request):
    return render(request, 'home/property-single-slider.html')



def page_contact(request):
    return render(request, 'home/page-contact.html')
