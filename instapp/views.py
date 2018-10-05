from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm

# Create your views here.
def Posts(request):
    Posts = Image.get_all()
    return render(request, 'index.html',{"Posts":Posts})


#.....
@login_required(login_url='/accounts/login/')
def NewPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = current_user
            new_post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'post.html', {"form": form})