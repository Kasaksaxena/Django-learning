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
    """data={
        'title':"Home page",
        'Name':"Kasak Saxena",
        "list":["python","java","PHP"],
        "Numbers":[5,40,90,7,30,10],
        "student_details":[
            {'name':'anita','phone':9856743215},
            {'name':"raj","phone":8547632514}
        ]
        
    }
    return render(request,"index.html",data)
    """
    
    return render(request,"index.html")

    