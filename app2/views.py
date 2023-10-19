from django.shortcuts import render

# Create your views here.
def renderTemplate2(request):
    return render(request, 'templatesApp/index2.html')

def renderAsia(request):
    datos = {"nombre": "Asia", "monumento1": "Gran Buda", "monumento2": "Gateaway of india", "monumento3":"Shwedagon Paya", "imagen1":"../static/images/Asia/Asia1.jpg", "imagen2":"../static/images/Asia/Asia2.jpg","imagen3": "../static/images/Asia/Asia3.jpg" }
    return render(request, 'templatesApp/index2.html',datos)