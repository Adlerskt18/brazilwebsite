from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Matches
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def resultPage(request):
    q = request.GET.get('q') if request.GET.get('q') != "None" else ''
    team = Matches.objects.filter(
            Q(match__icontains=q)
            )
    wins = Matches.objects.filter(
            Q(match__icontains=q) &
            Q(result__icontains="W")
            )
    context = {}
    if team and q != '':
        result = round((len(wins) / len(team)) * 100)
        context = {'result':result}
    else:
        messages.error(request, "Error")
        return redirect('index')
    
    return render(request, 'base/result_page.html', context)

def aboutPage(request):
    return render(request, 'base/about_page.html')
