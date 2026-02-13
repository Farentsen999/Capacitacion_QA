# TIPOS DE DATOS
# (en orden strin, int, float y bool)
A = "palabra"
B = 20
c = 3.14
D = False 

# LISTAS
Lista = ["palabra", 20, 3.14, False]

# DICCIONARIOS
Diccionario = {
    "string" : "palabra",
    "entero" : 20,
    "float" : 3.14,
    "bool" : False    
}

# Simulación de una respuesta de base de datos (API)
busqueda_panaderias = {
    "comuna": "Hualpén",
    "total_resultados": 3,
    "locales": [
        {
            "nombre": "Panadería El Sol",
            "rating": 4.5,
            "productos": ["Marraqueta", "Hallulla", "Empanada"],
            "abierto": True
        },
        {
            "nombre": "Amasandería Doña Rosa",
            "rating": 4.8,
            "productos": ["Pan de Molde", "Tortas"],
            "abierto": False
        },
        {
            "nombre": "Pan y Más",
            "rating": 3.9,
            "productos": ["Marraqueta", "Pasteles"],
            "abierto": True
        }
    ]
}


producto_panaderia__3 = busqueda_panaderias["locales"][2]["productos"][1]
print(producto_panaderia__3)

busqueda_panaderias["locales"][1]["abierto"] = True

promedio_rating = (busqueda_panaderias["locales"][0]["rating"] + busqueda_panaderias["locales"][1]["rating"] + busqueda_panaderias["locales"][2]["rating"]) / 3

but_report ={
    "id_bug" : 23,
    "severidad" : "Alta",
    "detalles" : ["Pan y Mas", 3.9]
}


