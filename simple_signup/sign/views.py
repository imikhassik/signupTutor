from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')
