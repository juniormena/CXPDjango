from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codigo= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=30)
    cedula=models.CharField(max_length=10)
    balance=models.PositiveIntegerField()
    estado=models.CharField(max_length=10)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)
    

class EntradaDocumento(models.Model):
    codigo= models.AutoField(primary_key=True)
    numeroDocumento = models.CharField(max_length=12, default="")
    numeroFactura = models.CharField(max_length=12, default="")
    fechaDocumento=models.DateField()
    monto = models.PositiveIntegerField()
    fechaRegistro=models.DateField()
    proveedor=models.CharField(max_length=50, default="")
    estado=models.CharField(max_length=20, default="")
    asiento_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        texto = "Documento no. {0} del proveedor ({1})"
        return texto.format(self.numeroDocumento, self.proveedor)
    
class Concepto(models.Model):
    codigo= models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=40)
    estado=models.CharField(max_length=10)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.descripcion, self.codigo)