from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def aboutUS(request):
    return render(request,"about.html")
    

def contactUS(request):
    print(request.method)
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"contact.html",{'output':output})

def Login(request):
    return render(request,"login-sginup.html")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def submitform(request):
    
    try:
        if request.method=="POST":
        #n1=int(request.GET['num1'])
        #n2=int(request.GET['num2'])
          n1=int(request.POST.get('num1'))
          n2=int(request.POST.get('num2'))
          finals=n1+n2
          data={
              'n1':n1,
              'n2':n2,
              'output':finals
          }
          
          return HttpResponse(finals)
    except:
     pass


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
    data={}
    try:
        if request.method=="POST":
        #n1=int(request.GET['num1'])
        #n2=int(request.GET['num2'])
          n1=int(request.POST.get('num1'))
          n2=int(request.POST.get('num2'))
          finals=n1+n2
          data={
              'n1':n1,
              'n2':n2,
              'output':finals
          }
          url="/contact-us/?output={}".format(finals)
          
          return HttpResponseRedirect(url)
    except:
        pass    
    return render(request,"form.html",data)
   