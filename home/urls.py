from django.urls import path, re_path
from .views import *



urlpatterns = [
    path('', index),
    path('index', index),
    path('home-map', home_map),
    path('home-property', home_property),
    path('home-splash', home_splash),

    path('agents', agents),
    path('agent-profile', agent_profile),
    path('agency-list', agency_list),
    path('agency-profile', agency_profile),

    path('service', service),
    path('service-details', service_details),

    path('page-about', page_about),
    path('page-contact', page_contact),
    path('page-faq', page_faq),
    path('page-404', page_404),


    path('blog', blog),
    path('blog-sidebar-right', blog_sidebar_right),
    path('blog-sidebar-left', blog_sidebar_left),
    path('blog-single', blog_single),

    path('user-profile', user_profile),
    path('social-profile', social_profile),
    path('my-properties', my_properties),
    path('favourite-properties', favourite_properties),
    #path('add-property', add_property),


    path('properties-grid', properties_grid),

    path('properties-grid-split', properties_grid_split),

    path('#', properties_list),
    path('properties-list', properties_list),
    path('properties-list-split', properties_list_split),
    path('property-single-gallery', property_single_gallery),
    path('property-single-slider', property_single_slider),

    path('page-contact', page_contact),


]
# path('properties-grid-split', properties_grid_split),