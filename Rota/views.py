from django.shortcuts import render

# Create your views here.

def rota(request):
    return render(request, 'rota/index.html')