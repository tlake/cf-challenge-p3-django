from django.conf.urls import patterns, include, url

# Commented line is the more flexible but older syntax:
#from users.views import user_list

# Next line replaces the above line, but for the newer class-based syntax:
from users.views import UserListView, UserDetailView, UserCreateView


urlpatterns = patterns('',
    # Commented pattern is for older syntax:
    #url(r'^$', user_list, name='user_list'),

    # Next line is newer class-based syntax:
    url(r'^$', UserListView.as_view(), name='user-list'),
    url(r'^(?P<pk>\d+)$', UserDetailView.as_view(), name='user-detail'),
    url(r'^create/', UserCreateView.as_view(), name='user-create'),
    )
