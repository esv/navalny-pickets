from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect

from picket.models import Picket

from django.conf import settings
from django.contrib.auth.decorators import login_required

def home(request):
    rows = Picket.objects.all()

    if request.user.is_authenticated():
        user_pickets = request.user.picket_set.all()
    else:
        user_pickets = []

    return render(request, 'home.html', {'rows':rows, 'user_pickets': user_pickets})

@login_required
def wont_go(request):
    # todo check existance
    p = Picket.objects.get(pk=request.POST.get('picket_id'))

    p.participants.remove(request.user)

    return HttpResponseRedirect('/')


@login_required
def go(request):

    # todo check existance
    p = Picket.objects.get(pk=request.POST.get('picket_id'))

    p.participants.add(request.user)

    return HttpResponseRedirect('/')

def auth_callback(request):
    return render(request, 'callback.html')