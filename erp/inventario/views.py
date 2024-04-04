from django.shortcuts import render
from inventario.models import Carro
import plotly.express as px
import pandas as pd
import random

def saludar(request):
    carros = Carro.objects.all()

    barrios = ["San Carlos", "San Vicente", "El Carmen", "Cedritos", "Chapinero", "San Benito", "Santa isabel", "Ciudad Bolivar"]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    # Generar datos para los 12 meses y varios años
    datos = {"Barrio": [], "Ventas": [], "Mes": [], "Año": []}
    for _ in range(100):  # Generar 100 registros aleatorios
        for barrio in barrios:
            for mes in meses:
                ventas = random.randint(10, 1000)  # Generar un número aleatorio entre 10 y 1000 para las ventas
                año = random.randint(2020, 2023)  # Generar un año aleatorio entre 2020 y 2023
                datos["Barrio"].append(barrio)
                datos["Ventas"].append(ventas)
                datos["Mes"].append(mes)
                datos["Año"].append(año)

    # Convertir el diccionario de datos en un DataFrame de pandas
    df = pd.DataFrame(datos)

    # Crear el gráfico de barras
    grafico = px.bar(df, x="Barrio", y="Ventas", color="Mes", facet_row="Año", category_orders={"Mes": meses})

    # Convertir el gráfico a HTML
    mihtml = grafico.to_html(full_html=False)

    context = {
        "nombre": "Santiago",
        "carros": carros,
        "grafica": mihtml
    }
    return render(request, "inventario/index.html", context)
