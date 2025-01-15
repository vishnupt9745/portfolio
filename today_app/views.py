from django.shortcuts import render

# Create your views here.

def first_template(request):
    return render(request,'today1.html')


def second_template(request):
    return render(request,'second.html')

def index(request):
    return render(request,'index.html')
