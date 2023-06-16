from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})

# if a user is not logged in, it redirects to the /admin
# endpoint to login
@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
