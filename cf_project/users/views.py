'''

This commented block is a view function done in an older style which is quite
flexible, but requires a lot more typing - this interferes with the DNRY principle.

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from users.models import User

def user_list(request):
        user = User.objects.all()
        return render_to_response('users/user_list.html', {'object_list': user}, context_instance=RequestContext(request))
'''

# This is a newer 'class-based generic view' setup; less typing, but this syntax
# isn't as flexible.
#
# I guess the lesson is to prefer this method, but be bale to fall back on the
# older syntax if necessary?

from users.models import User
from django.views.generic import ListView, DetailView, CreateView

class UserListView(ListView):
    model = User

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
