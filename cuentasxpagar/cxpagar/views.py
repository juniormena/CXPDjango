from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido a Cuentas por Pagar</h1>")

def conceptos(request):
    return render(request, 'conceptos/index.html')   

def crear_concepto(request):
    return render(request, 'conceptos/crear.html')   

def editar_concepto(request):
    return render(request, 'conceptos/editar.html')  