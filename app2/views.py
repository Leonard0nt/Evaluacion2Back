from django.shortcuts import render

# Create your views here.
def renderTemplate2(request):
    return render(request, 'templatesApp/index2.html')

def renderAsia(request):
    datos = {"nombre": "Asia", "monumento1": "Gran Buda", "monumento2": "Gateaway of india", "monumento3":"Shwedagon Paya", "imagen1":"../static/images/Asia/Asia1.jpg", "imagen2":"../static/images/Asia/Asia2.jpg","imagen3": "../static/images/Asia/Asia3.jpg" }
    return render(request, 'templatesApp/index2.html',datos)

def renderAmerica(request):
    datos = {"nombre": "America", "monumento1": "Cristo Redentor", "monumento2": "Moai", "monumento3":"Monte RushMore", "imagen1":"../static/images/America/America1.jpg", "imagen2":"../static/images/America/America2.jpg","imagen3": "../static/images/America/America3.jpg" }
    return render(request, 'templatesApp/index2.html',datos)

def renderEuropa(request):
    datos = {"nombre": "Europa", "monumento1": "Torre Eifel", "monumento2": "Torre de Pizza", "monumento3":"Coliseo Romano", "imagen1":"../static/images/Europa/Europa1.jpg", "imagen2":"../static/images/Europa/Europa2.jpg","imagen3": "../static/images/Europa/Europa3.jpg" }
    return render(request, 'templatesApp/index2.html',datos)