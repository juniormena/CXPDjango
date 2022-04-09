from datetime import datetime
from django.shortcuts import redirect, render
from cuentasxpagarapp.models import Proveedor, EntradaDocumento, Concepto
from django.contrib.auth.decorators import login_required
import requests

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

def getConcepto(codigo = 0):
    if codigo == 0:
        return Concepto.objects.all()
    else:
        return Concepto.objects.get(codigo=codigo)

#render homePage
@login_required(login_url='/login/')
def home(request):
    return render(request, "./Home/Home.html")

# CRUD Proveedores
@login_required(login_url='/login/')
def proveedores(request):
    proveedores = getProveedor()
    return render(request, "gestionProve.html",{"proveedores":proveedores})

@login_required(login_url='/login/')
def registrarproveedor(request):
    nombre= request.POST['Nombre']
    tipo= request.POST['Tipo']
    cedula= request.POST['Cedula']
    balance= request.POST['Balance']
    estado= request.POST['Estado']

    Proveedor.objects.create(nombre=nombre, tipo=tipo, cedula=cedula, balance=balance, estado=estado)
    return redirect(redirect_to)

@login_required(login_url='/login/')
def edicionProve(request, codigo):
    proveedor = getProveedor(codigo)
    return render(request, "edicionProve.html", {"proveedor":proveedor})

@login_required(login_url='/login/')
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
    
@login_required(login_url='/login/')
def eliminarProve(request, codigo):
    proveedor = getProveedor(codigo)
    proveedor.delete()

    return redirect (redirect_to)


#CRUD conceptos
@login_required(login_url='/login/')
def conceptos(request):
    conceptosPago = getConcepto()
    data= {"conceptos":conceptosPago}
    return render(request, "./conceptos/gestionCon.html", data)


@login_required(login_url='/login/')
def addConcepto(request):
    descripcion= request.POST['descripcion']
    estado = request.POST['estado']

    Concepto.objects.create(descripcion=descripcion, estado=estado)
    return redirect('/conceptos')

@login_required(login_url='/login/')
def editConcepto(request, codigoConcepto):
    if request.method == 'GET':
        concepto = getConcepto(codigoConcepto)
        data = {"concepto":concepto}
        return render(request, "./Conceptos/edicionCon.html", data)
    elif request.method == 'POST':
        descripcion= request.POST['descripcion']
        estado = request.POST['estado']
        
        concepto = getConcepto(codigoConcepto)
        concepto.descripcion = descripcion
        concepto.estado = estado
        concepto.save()
        return redirect('/conceptos')
   
    return redirect('/conceptos')

@login_required(login_url='/login/')
def deleteConcepto(request, codigoConcepto):
    Concepto = getConcepto(codigoConcepto)
    Concepto.delete()

    return redirect ('/conceptos')



#CRUD Entrada Documentos
@login_required(login_url='/login/')
def entradaDocumentos(request):
    entradaDocumentos = getEntradaDocumento()
    proveedores = getProveedor(0, 'EntradaDocumentos')
    today = datetime.now().strftime("%Y-%m-%d")
    data= {"entradaDocumentos":entradaDocumentos, "proveedores":proveedores, "today": today}
    return render(request, "./EntradaDocumentos/gestionEntradaDocumentos.html", data )

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def crearAsiento(request):
    sum = 0
    fechaDesde= request.POST['fechaDesde']
    fechaHasta= request.POST['fechaHasta']
    data= EntradaDocumento.objects.filter(fechaDocumento__range=(fechaDesde, fechaHasta)).exclude( estado = 'Contabilizado')
    if(len(data) == 0):
       return redirect('/noData')
    url = "https://contabilidad-api.azurewebsites.net/asientos_contables"
    for dat in data:
        sum = sum + dat.monto
    payload= {
        'descripcion': 'asiento de CXP',
        'idSistemaAuxiliar': 6,
        'idCuentaCredito': 82,
        'idCuentDebito': 82,
        'monto': sum
    }
    headers = {'Content-type': 'application/json'}
    
    r = requests.post(url, json = payload, headers=headers)
    if r.json().get('id'):
        data2 = r.json()
        data.update(asiento_id = data2.get('id'), estado = 'Contabilizado', monto = sum)
    return redirect('/entradaDocumentos')

    

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def deleteEntradaDocumento(request, codigoEntradaDocumento):
    proveedor = getEntradaDocumento(codigoEntradaDocumento)
    proveedor.delete()

    return redirect ('/entradaDocumentos')

@login_required(login_url='/login/')
def noData(request):
    return render(request, "./noData/noData.html")