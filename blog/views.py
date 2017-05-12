#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    return HttpResponse('<h1>Page was found</h1>')
    #return render_to_response('index.html',{'blog_list':blog_list})
