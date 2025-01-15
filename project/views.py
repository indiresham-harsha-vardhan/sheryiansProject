from django.shortcuts import render,redirect
from .models import *
from .form import *
# Create your views here.
def main(request):
    return render(request,'main.html')
def home(request):
    data=cou.objects.all()
    return render(request,'home.html',{'data':data})
def course(request):
    data=cou.objects.all()
    return render(request,'course.html',{'data':data})
def Bootcamp(request):
    return render(request,'Bootcamp.html')
def RequestCallBack(request):
    if request.method=='POST':
        obj=reform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('project:home')
    return render(request,'RequestCallBack.html')
def sign(request):
    if request.method=='POST':
        f=signform(request.POST)
        if f.is_valid():
            print('hi')
            f.save()
            return redirect('project:home')
    return render(request,'sign.html')
