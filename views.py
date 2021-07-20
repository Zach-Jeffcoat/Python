from django.shortcuts import render, redirect


# Create your views here.

from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs!");

def new(request):
    return HttpResponse("placeholder to display a new form to creaate a blog!");

def create(request):
    return(redirect('/'))

def show(request, number):
    return HttpResponse(f"placeholder to display blog number {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def delete(request, number):
    return(redirect('/'))
