from django.urls import path
from .views import create


urlpatterns = [

    path('create', create),

]


#re_path
#details, edit, delete

# re_path(r'^details/(?P<post_id>[0-9]+)$', details),
# re_path(r'^edit/(?P<post_id>[0-9]+)$', edit),
# re_path(r'^delete/(?P<post_id>[0-9]+)$', delete)