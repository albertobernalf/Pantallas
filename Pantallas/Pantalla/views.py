from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, View
import requests

import json
from django.http import HttpResponse, JsonResponse

# Create your views here.

class salidaView(TemplateView):
    print("Entre Inicio5")
    template_name = 'salida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi Inicio'
       
        return context

    def post(self, request, *args, **kwargs):
        print("Entre POST salida.html")

        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        acceso = request.POST.get('acceso')
        print(codigo)
        print(nombre)
        print(acceso)
        datos = {}
        context = {}
        datos['codigo'] = codigo
        datos['nombre'] = nombre
        datos['acceso'] = acceso

        print(datos['codigo'])

        if datos['codigo'] == '0':
            print("Opcion 0")
            return render(request, 'inicio4.html', context)

        if datos['codigo'] == '1':
            print("Opcion 1")
            context['nombre'] = datos['nombre']
            return render(request, 'inicio5.html', context)

        if datos['codigo'] == '2':
            print("Opcion 2")
            return render(request, 'inicio6.html', context)




def data(request):
    print("Entre datos")

    datos = {}
    context = {}

    if request.method == 'POST' :
        print("Entre POST DE data ")
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        acceso = request.POST.get('acceso')
        datos['codigo'] = codigo
        datos['nombre'] = nombre
        datos['acceso'] = acceso

    print(datos['codigo'])
    print(datos['nombre'])
    print(datos['acceso'])

    if datos['codigo'] == '0':
        print("Opcion 0 Me voy a pintar la pagina")
        return render(request, 'inicio4.html', datos)

    if datos['codigo'] == '1':
        print("Opcion 1")
        context['nombre'] = datos['nombre']
        return render(request, 'inicio5.html', context)

    if datos['codigo'] == '2':
        print("Opcion 2")
        return render(request, 'inicio6.html', context)


def data1(request):
    print("Entre sdata1")
    url = "http://localhost:8000/data/"
    url2 = "http://localhost:8000/data2/"
    datos = {'codigo' : '0' , 'nombre' : 'Alexander', 'acceso':'Restringido'}
    # datos = {'app_key' : 'jac2021-791' , 'id_pi' : '10', 'rf_id':'060060B37DA8'}
    response = requests.post(url, data=datos)
    print("PASE")
    parametros = {'codigo': '0', 'nombre': 'Alberto', 'acceso' : 'Autorizado'}

    response2 = requests.get(url2,  params=parametros)
    print("PASE2")

    if response.status_code == 200:
       ## print(response.content)
       print(response.text)
      # print (response.json())

    if response2.status_code == 200:
        ## print(response.content)
        print(response2.text)
        #  print(response2.json())


    return render(request, 'inicio4.html', datos)
    #return HttpResponse("Ok ! ")


def data2(request):
    print("Entre sdata1")
    context = {}
    return render(request, 'salida2.html', context)


