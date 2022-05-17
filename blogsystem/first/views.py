from colorsys import TWO_THIRD
from importlib import import_module
from pyexpat.errors import messages
from urllib import response
#samruddhi add model here
from first.models import reg
#upto this
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def technology(request):
    return render (request, 'technology.html')


def writting(request):
    return render (request, 'writting.html')

#make change by samruddhi
def saveRegister(request):
    if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            pass1=request.POST.get("pass1")
            re_pass=request.POST.get("re_pass")
            en=reg(name=name,email=email,pass1=pass1,re_pass=re_pass)
            en.save()
    return render(request, 'signup.html')


#def index(request):
 #   return render (request, 'social media.html')



    # else:
    #     return HttpResponse('not found')

    



def login(request):
    return render(request, 'login.html')

#    two = request.GET.get('two')
#    if two is not None:
#        return redirect('/login/')
#    else:
#        return render(request, 'login.html')


def register(request):
    
    
  
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['re_pass']

        # 2 may check for arrorneous inputs
        if len(username)>50:
            messages.error(request,"username must be under must be under 10 characters")
            return redirect('login')
            
        # 2 may 
        if not username.isalnum():
            messages.error(request,"username should only contaion letters and numbers")
            return redirect('login')
       
        if pass1 != pass2:
            messages.error(request,"password do not match")
            return redirect('login')
    return render(request, 'register.html')
        #else: return  HttpResponse('not found')


      



         #myuser = User.objects.create_user(username, email, pass1)
         #myuser.first_name = fname
         #myuser.last_name = lname
         #myuser.save()
        # messages.success(request, 'your account is created')
        

    


