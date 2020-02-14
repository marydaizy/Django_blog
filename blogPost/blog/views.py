from django.shortcuts import render
from .models import Post

# Create your views here.
 
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def register(request):
    return render(request, 'blog/register.html', {'title':'Register'})

def login(request):
    return render(request, 'blog/login.html', {'title':'Login'})