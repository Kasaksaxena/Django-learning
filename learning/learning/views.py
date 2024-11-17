from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Userforms

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

def calculator(request):
    c=''
    try:
        if request.method=="Post":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num2"))
            opr=request.POST.get("opr")
            
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
            elif opr=="%":
                c=n1%n2
            
              
                
    except:
        c="Invalid operator" 
        print(c)  
    return render(request,"calculator.html",{"result":c})

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
    fn=Userforms()
    data={'form':fn}
    try:
        if request.method=="POST":
        #n1=int(request.GET['num1'])
        #n2=int(request.GET['num2'])
          n1=int(request.POST.get('num1'))
          n2=int(request.POST.get('num2'))
          finals=n1+n2
          data={
              'form':fn,
              
              'output':finals
          }
          url="/contact-us/?output={}".format(finals)
          
          return HttpResponseRedirect(url)
    except:
        pass    
    return render(request,"form.html",data)
   