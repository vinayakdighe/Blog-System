from colorsys import TWO_THIRD
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
   q = request.GET.get('q')
   if q is not None:
       return redirect('/signup/')
   else:
       return render(request, 'signup.html')

def login(request):
   two = request.GET.get('two')
   if two is not None:
       return redirect('/login/')
   else:
       return render(request, 'login.html')
