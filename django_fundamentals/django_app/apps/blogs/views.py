from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

# Create your views here.
def temp(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    response = "Redirecting back to Home"
    return HttpResponseRedirect("/")

def show(request):
    response =  "placeholder to display blog {{number}}"
    return HttpResponse(response)

def edit(request):
    response =  "placeholder to edit blog {{number}}"
    return HttpResponse(response)

def destroy(request):
    response = "redirecting back to Home"
    return HttpResponseRedirect("/")
