from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def showblogs(request):
    blogs = Blog.objects.all().order_by('-pub_date')
    context = {
        'blogs' : blogs,
    }
    return render(request, 'blog/allblogs.html', context)

def detail(request, blog_id):
    #blog_detail = Blog.objects.get(id = blog_id)
    blog_detail = get_object_or_404(Blog, pk=blog_id)   
    context = {
        'blog_detail' : blog_detail,
    } 
    return render(request, 'blog/blog_detail.html', context)
    