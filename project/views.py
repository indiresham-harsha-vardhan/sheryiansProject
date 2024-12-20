from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')
def home(request):
    return render(request,'home.html')
def course(request):
    return render(request,'course.html')
def Bootcamp(request):
    return render(request,'Bootcamp.html')
def RequestCallBack(request):
    return render(request,'RequestCallBack.html')
def sign(request):
    return render(request,'sign.html')
