from django.http import HttpResponse

def aboutUS(request):
    return HttpResponse("Hello World")

def contactUS(request):
    return HttpResponse("<b>Hello Kasak Saxena </b>")

def Course(request):
    return HttpResponse("Nice to Meet you")

def courseDetails(request,courseid):
    return HttpResponse(courseid)
    