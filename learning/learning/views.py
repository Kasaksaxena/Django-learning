from django.http import HttpResponse
from django.shortcuts import render

def aboutUS(request):
    return HttpResponse("Hello World")

def contactUS(request):
    return HttpResponse("<b>Hello Kasak Saxena </b>")

def Course(request):
    return HttpResponse("Nice to Meet you")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def homePage(request):
    data={
        'title':"Home page",
        'Name':"Kasak Saxena"
    }
    return render(request,"index.html",data)
    