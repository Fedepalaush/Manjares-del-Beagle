from django.shortcuts import render

# Create your View here.


def index(request):
 return render (request, 'index.html')