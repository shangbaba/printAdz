from django.shortcuts import render

def myblog(request):
    return render(request, 'blog/myblog.html')

def index(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')