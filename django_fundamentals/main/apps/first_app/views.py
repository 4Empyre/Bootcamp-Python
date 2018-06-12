from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# the index function is called when root is visited
print "This is main/views.py" #for testing

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def test(request):
    response = "Hello, I am test."
    return HttpResponse(response)
