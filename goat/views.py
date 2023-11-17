from django.shortcuts import render

# Create your views here.
def goat(request):
    return render(request,'goat.html')
