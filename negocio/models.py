from django.db import models

# Create your models here.
class Producto(models.Model):
    imagen = models.ImageField()
    descripcion = models.TextField(max_length=100)
    precio = models.TextField(max_length=10)
    stock = models.TextField(max_length=5)
    marca = models.TextField(max_length=20)
    codigo = models.TextField(max_length=100)
    
    def __str__(self):
        return self.codigo
        

class Cliente(models.Model):
    rut = models.TextField(max_length=12, primary_key=True)
    nombre = models.TextField(max_length=100)
    correo = models.TextField(max_length=100)
    telefono = models.TextField(max_length=10)
    
    def __str__(self):
        return self.nombre

class Carro(models.Model):
    codProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.TextField(max_length=10)
    rutCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
        
        
