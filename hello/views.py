from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def new (request):
   return render(request,'hello.html')
def counter(request):
   text=request.GET['text']
   ammount_of_words=len(text.split())
   return render(request,counter.html,{'words':ammount_of_words})
