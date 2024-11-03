from django.http import HttpResponse
from django.shortcuts import render

def aboutUS(request):
    return render(request,"about.html")
    

def contactUS(request):
    return render(request,"contact.html")

def Login(request):
    return render(request,"login-sginup.html")

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

def form(request):
    finals=0
    try:
        #n1=int(request.GET['num1'])
        #n2=int(request.GET['num2'])
        n1=int(request.GET.get('num1'))
        n2=int(request.GET.get('num2'))
        finals=n1+n2
    except:
        pass    
    return render(request,"form.html",{'output': finals})
   