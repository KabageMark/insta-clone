from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewPostForm,NewProfileForm
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


@login_required(login_url='/accounts/login/')
def Update(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_update = form.save()
            new_update.user = current_user
            new_update.save()
        return redirect('index')

    else:
        form = NewProfileForm()
    return render(request, 'post.html', {"form": form})