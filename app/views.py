from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    return render(request, 'templatesApp/index.html')

def renderProductosElectro(request):
    datos = {"nombre": "Electronica", "producto1": "Mac", "producto2": "Iphone", "producto3":"PlayStation", "imagen":"../static/images/producto.jpg"}
    return render(request, 'templatesApp/producto.html',datos)

def renderProductosJuguetes(request):
    datos = {"nombre": "Juguetes", "producto1": "Auto", "producto2": "Pelota", "producto3":"Figura", "imagen":"../static/images/producto.jpg"}
    return render(request, 'templatesApp/producto.html',datos)

def renderProductosRopa(request):
    datos = {"nombre": "Ropa", "producto1": "Pantalones", "producto2": "Chaqueta", "producto3":"Camisa", "imagen":"../static/images/producto.jpg"}
    return render(request, 'templatesApp/producto.html',datos)


