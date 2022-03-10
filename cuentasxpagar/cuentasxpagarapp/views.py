from datetime import datetime
from tkinter.messagebox import RETRY
from xml.dom.minidom import Identified
from django.shortcuts import redirect, render
from cuentasxpagarapp.models import Proveedor, EntradaDocumento
from datetime import datetime

# Create your views here.

redirect_to = '/proveedores'

def getProveedor(codigo = 0, desde = 'Proveedores'):
    if codigo == 0 and desde == 'Proveedores':
        return Proveedor.objects.all()
    elif codigo == 0 and desde == 'EntradaDocumentos':
        return Proveedor.objects.filter(estado='Activo')
    else:
        return Proveedor.objects.get(codigo=codigo)

def getEntradaDocumento(codigo = 0):
    if codigo == 0:
        return EntradaDocumento.objects.all()
    else:
        return EntradaDocumento.objects.get(codigo=codigo)

def home(request):
    return render(request, "./Home/Home.html")

# CRUD Proveedores
def proveedores(request):
    proveedores = getProveedor()
    return render(request, "gestionProve.html",{"proveedores":proveedores})

def registrarproveedor(request):
    nombre= request.POST['Nombre']
    tipo= request.POST['Tipo']
    cedula= request.POST['Cedula']
    balance= request.POST['Balance']
    estado= request.POST['Estado']

    Proveedor.objects.create(nombre=nombre, tipo=tipo, cedula=cedula, balance=balance, estado=estado)
    return redirect(redirect_to)


def edicionProve(request, codigo):
    proveedor = getProveedor(codigo)
    return render(request, "edicionProve.html", {"proveedor":proveedor})

def editarProve(request, codigo):
    nombre= request.POST['Nombre']
    tipo= request.POST['Tipo']
    cedula= request.POST['Cedula']
    balance= request.POST['Balance']
    estado= request.POST['Estado']  
    proveedor = getProveedor(codigo)
    proveedor.nombre = nombre
    proveedor.tipo = tipo
    proveedor.cedula = cedula
    proveedor.balance = balance
    proveedor.estado = estado
    proveedor.save()
    return redirect (redirect_to)
    

def eliminarProve(request, codigo):
    proveedor = getProveedor(codigo)
    proveedor.delete()

    return redirect (redirect_to)


#CRUD Entrada Documentos

def entradaDocumentos(request):
    entradaDocumentos = getEntradaDocumento()
    proveedores = getProveedor(0, 'EntradaDocumentos')
    today = datetime.now().strftime("%Y-%m-%d")
    data= {"entradaDocumentos":entradaDocumentos, "proveedores":proveedores, "today": today}
    return render(request, "./EntradaDocumentos/gestionEntradaDocumentos.html", data )

def addEntradaDocumento(request):
    numeroDocumento= request.POST['numeroDocumento']
    numeroFactura= request.POST['numeroFactura']
    fechaDocumento = request.POST['fechaDocumento']
    monto = request.POST['monto']
    fechaRegistro = request.POST['fechaRegistro']
    proveedor = request.POST['proveedor']
    estado = request.POST['estado']

    EntradaDocumento.objects.create(numeroDocumento=numeroDocumento, numeroFactura=numeroFactura, fechaDocumento=fechaDocumento, monto=monto, fechaRegistro=fechaRegistro, proveedor=proveedor, estado=estado)
    return redirect('/entradaDocumentos')

def editEntradaDocumento(request, codigoEntradaDocumento):
    if request.method == 'GET':
        entradaDocumento = getEntradaDocumento(codigoEntradaDocumento)
        proveedores = getProveedor(0, 'EntradaDocumentos')
        data = {"entradaDocumento":entradaDocumento, "proveedores":proveedores}
        return render(request, "./EntradaDocumentos/edicionEntradaDocumento.html", data)
    elif request.method == 'POST':
        numeroDocumento= request.POST['numeroDocumento']
        numeroFactura= request.POST['numeroFactura']
        fechaDocumento = request.POST['fechaDocumento']
        monto = request.POST['monto']
        fechaRegistro = request.POST['fechaRegistro']
        proveedor = request.POST['proveedor']
        estado = request.POST['estado']
        
        entradaDocumento = getEntradaDocumento(codigoEntradaDocumento)
        entradaDocumento.numeroDocumento = numeroDocumento
        entradaDocumento.numeroFactura = numeroFactura
        entradaDocumento.fechaDocumento = fechaDocumento
        entradaDocumento.monto = monto
        entradaDocumento.fechaRegistro = fechaRegistro
        entradaDocumento.proveedor = proveedor
        entradaDocumento.estado = estado
        entradaDocumento.save()
        return redirect('/entradaDocumentos')
   
    return redirect('/entradaDocumentos')

def deleteEntradaDocumento(request, codigoEntradaDocumento):
    proveedor = getEntradaDocumento(codigoEntradaDocumento)
    proveedor.delete()

    return redirect ('/entradaDocumentos')