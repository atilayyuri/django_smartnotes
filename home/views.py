from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

# if a user is not logged in, it redirects to the /admin
# endpoint to login

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
