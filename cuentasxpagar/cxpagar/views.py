from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido a Cuentas por Pagar</h1>")

def conceptos(request):
    return render(request, 'paginas/conceptos.html')    