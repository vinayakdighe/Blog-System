from colorsys import TWO_THIRD
from pyexpat.errors import messages
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'your account is created')
        return render(request, 'signup.html')

    else:
        return HttpResponse('not found')

    



def login(request):
    return render(request, 'login.html')

#    two = request.GET.get('two')
#    if two is not None:
#        return redirect('/login/')
#    else:
#        return render(request, 'login.html')




