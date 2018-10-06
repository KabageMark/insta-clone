from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewPostForm
from .models import Image
# Create your views here.
def Posts(request):
    posts = Image.get_all()
    return render(request, 'index.html',{"posts":posts,})


#.....
@login_required(login_url='/accounts/login/')
def NewPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            new_post.user = current_user
            new_post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'post.html', {"form": form})