from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def fa(request):
    return render(request,'pages/fa.html')


def loginA(request):
    return render(request,'pages/loginA.html')