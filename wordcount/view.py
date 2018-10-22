from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    text = request.GET['text'] # note []
    li = text.split()
    words = { name:li.count(name) for name in li }
    words = sorted(words.items(),key = operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'words':words, 'n':len(li)})

def about(request):
    return render(request, 'about.html')