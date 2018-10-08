from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewPostForm,NewProfileForm
from .models import Image,Profile

# Create your views here.
def Posts(request):
    posts = Image.get_all()
    return render(request, 'index.html',{"posts":posts,})

def Profiles(request):
    profile = Profile.get_all()
    return render(request, 'profiles.html',{"profile":profile,})

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
        return redirect('profile')

    else:
        form = NewProfileForm()
    return render(request, 'update.html', {"form": form})



def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_username(search_term)
        message = f"{search_term}"
        
        return render(request, 'searched.html',{"message":message,"searched_profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searched.html',{"message":message}) 