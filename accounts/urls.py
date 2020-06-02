from django.urls import path
from .views import sign_in, sign_up, sign_out, profile, ajax_reg, user_profile
from .views import *


urlpatterns = [
    path('sign_in', sign_in),
    path('sign_up', sign_up),
    path('sign_out', sign_out),
    path('profile', profile),
    path('user-profile', user_profile),
    path('user-profile', user_profile),
    path('social-profile', social_profile),
    path('my-properties', my_properties),
    path('favourite-properties', favourite_properties),
    path('add-property', add_property),

    path('ajax_reg', ajax_reg)

]
