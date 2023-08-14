from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import post

# Create your views here.


def view(req):
    posts = post.objects.all()
    data = [{'userName':post.userName, 'posts':post.posts} for post in posts]

    res = json.dump(data)
    return HttpResponse(res, content_type = 'application/json')


def deleting(req, post_id):
      try:
        posts = post.objects.get(id = post_id)
        posts.delete()
        return HttpResponse(json.dumps({'msg':'Post deleted'}), content_type = 'application/json')
    