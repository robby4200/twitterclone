
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Post
from .forms import PostForm


# Create your views here.

def index(request):
    print("hello world")

    if request.method=='POST':

        form = PostForm(request.POST,request.FILES)
        

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20] 


    return render(request,'posts.html',
                 {'posts': posts})



def delete(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")

def update(request,post_id):
    posts=Post.objects.get(id=post_id)
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('notvalid')
    return render(request, "update.html",{'posts':posts})

def like(request,post_id):
    newlikecount=Post.objects.get(id=post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect("/")