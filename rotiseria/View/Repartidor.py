from django.shortcuts import render, redirect


def mapa(request):
    return render (request,'Repartidor/index.html')