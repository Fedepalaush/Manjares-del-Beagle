from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def mapa(request):
    return render (request,'Repartidor/index.html')