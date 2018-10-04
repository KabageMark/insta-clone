from django.shortcuts import render,request

# Create your views here.
def register(request):
    return render(request,'registration/registration_form.html',)
