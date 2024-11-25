from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import Userforms
from service.models import Service

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
    #serviceData=Service.objects.all() // extract table data
    serviceData=Service.objects.all().order_by('-service_title')[2:5]#cant use negative slicing
    #descendirng order
    # use for loop in the html section to implement
    
    data={
        'serviceData':serviceData
        
    }
    """ Template filters 
    ex- {{n,service_des |safe}},{{n,service_des |lower}},{{n,service_des |upper}}
    """
    
    
    
    
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
    
    return render(request,"index.html",data)

def marksheet(request):
    if request.method== "POST":
        if request.POST.get('subject1')=="":
            return render(request,"marksheet.html",{"error":True})
        
        s1=eval(request.POST.get("subject1"))
        s2=eval(request.POST.get("subject2"))
        s3=eval(request.POST.get("subject3"))
        s4=eval(request.POST.get("subject4"))
        s5=eval(request.POST.get("subject5"))
        t=s1+s2+s3+s4+s5
        p=t*100/500
        if p>=80:
            d="First division"
        elif p>=60:
            d=" Second division division"
        elif p>=40:
            d=" Third division"
        else:
            p>=70
            d="FAIL"
            
        data={
             "total":t,
             "per":p,
             "div":d
         }  
        return render(request,"marksheet.html",data) 
        
        
        
    return render(request,"marksheet.html")    
        

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
   