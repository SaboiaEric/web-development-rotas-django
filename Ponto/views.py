from django.shortcuts import render

# Create your views here.

def ponto(request):
    return render(request, 'ponto/index.html')
    