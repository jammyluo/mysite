#coding:utf-8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from myapp.models import BlogsPost

# Create your views here.
def list_posts(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("list.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))