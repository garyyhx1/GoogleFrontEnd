from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request, "UCLAwiki/index.html")
def edit(request):

    return render(request, "UCLAwiki/edit.html")