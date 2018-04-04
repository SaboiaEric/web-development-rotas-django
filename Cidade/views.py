from django.shortcuts import render

# Create your views here.

def cidade(request):
    return render(request, 'cidade/index.html')
    