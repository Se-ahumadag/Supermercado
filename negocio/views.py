from django.shortcuts import render
from negocio.models import Producto
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

    
def Inicio(request):
    return render(request, 'Portada.html', {})
    
def registro(request):

    if request.method == "POST":
        nombre = request.POST["txtNombre"]
        correo = request.POST["txtCorreo"]
        clave = request.POST["txtClave"]
        User.objects.create(username=nombre, email=correo, password=make_password(clave))
        
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        
    else:
        return render(request, 'registro.html', {})
    
def Galeria(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    mensaje = ""
    lista = {}
    lista = Producto.objects.all()
    
    
    contexto = {'mensaje': mensaje, 'lista':lista}
    return render(request, 'Galeria.html', {})
    
def RegistroProductos(request):
    mensaje = ""
    lista = {}
    item = {}
    
    if request.method == "POST":
        codigo = int("0" + request.POST["txtCodigo"])
        imagen = request.POST["fileImagen"]
        descripcion = request.POST["txtDescripcion"]
        precio = request.POST["txtPrecio"]
        stock = request.POST["txtStock"]
        marca = request.POST["txtMarca"]        
        
        if 'btnGrabar' in request.POST:
            if codigo < 1:                
                Producto.objects.create(imagen = imagen, descripcion = descripcion, precio = precio, stock = stock, marca = marca)                
             
            else:
                item = Producto.objects.get(pk = codigo)
                item.imagen = imagen
                item.descripcion = descripcion
                item.precio = precio
                item.stock = stock
                item.marca = marca
                item.save()
                item = {}
            mensaje = "Datos Guardados"
        elif 'btnBuscar' in request.POST:
            try:
                item = Producto.objects.get(pk = codigo)
            except:
                mensaje = "Registro no encontrado"
                item = {}
                
        elif 'btnListar' in request.POST:
            lista = Producto.objects.all()
            
        elif 'btnEliminar' in request.POST:
            item = Producto.objects.get(pk = codigo)
            item.delete()
            mensaje = "Registro Eliminado"
            item = {}
    
    contexto = {'mensaje': mensaje, 'lista':lista , 'item':item}
        

    return render(request, 'RegistroProductos.html', contexto)