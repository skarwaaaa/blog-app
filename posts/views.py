from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
  # return HttpResponse("Hello World!")
  posts = Post.objects.order_by('-published')
  return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, post_id):
  post = Post.objects.get(pk=post_id)#pk= indexの番号のこと
  return render(request, 'posts/post_detail.html', {'post':post})