from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Blog
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')
    
def price(request):
    return render(request, 'home/price.html')

def how_it_works(request):
    return render(request, 'home/how_it_work.html')

def about(request):
    return render(request, 'home/about.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'home/blog.html', {'blogs': blogs})

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blogs = Blog.objects.all()
    context = {
        'blog': blog,
        'blogs': blogs
    }
    return render(request, 'home/blog_details.html', context)