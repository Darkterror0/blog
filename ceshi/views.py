from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'新智慧领导.html')