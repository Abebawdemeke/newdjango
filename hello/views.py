from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def new (request):
    # return HttpResponse("<h1> how is it going? </h1>")
   return render(request,'hello.html')