from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . forms import MakePost


def index(request):
    return render(request,"index.html")
def user(request):
    if request.method =='POST':
        form= MakePost(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>') 
    form=MakePost()
    return render(request,"user.html",{'form':form})