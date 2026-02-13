#Aprovecha las funciones para realizar la menor cantiad de cambios al codigo para adaptarte a los
#cambios del sistema

def validar_peso(peso, limite):
    try:
        if peso == None:
            return None
        else:
            peso = int(float(peso))
            if(peso <= limite):
                return True
            else:
                return False
    except (ValueError, TypeError): 
        return None

def verificar_seguridad(tipo, es_peligroso, peso):
    try:
        if peso == None:
            return None
        else:
            peso = int(float(peso))
            if tipo != "Standard" and es_peligroso == True:
                return False
            elif tipo == "Reefer" and peso >=18000:
                return False
            else:
                return True
    except (ValueError, TypeError): 
        return None
    
def generar_log(contenedor_id, mensaje, estado):
    try: 
        print(f"{estado} - {contenedor_id} | Motivo: {mensaje}")
    except (ValueError, TypeError):
        print("ERROR LOS DATOS NO ESTAN ASOSIADOS A NINGUN CONTENEDOR")
        return None
    
    
def procesar_manifiesto(lista_contenedores, contenedores_aprobados, contenedores_rechazados):
    limite = 20000    
    for i in lista_contenedores:
        peso_adecuado = validar_peso(i.get('peso'), limite)
        seguridad_verificada = verificar_seguridad(i.get('tipo'),i.get('peligroso'),i.get('peso'))
        
        if peso_adecuado == True and seguridad_verificada == True:
            contenedores_aprobados.append(i)
            generar_log(i.get('id'),"El contenedor cumple con los requisitos", "ACEPTADO")
            
        elif peso_adecuado == False and seguridad_verificada == True:
            contenedores_rechazados.append(i)
            generar_log(i.get('id'),"El contenedor no cumple con los requisitos de seguridad", "RECHAZADO")
        elif peso_adecuado == True and seguridad_verificada == False:
            contenedores_rechazados.append(i)
            generar_log(i.get('id'),"El contenedor no cumple con los requisitos de peso", "RECHAZADO")
        elif peso_adecuado == False and seguridad_verificada == False:
            contenedores_rechazados.append(i)
            generar_log(i.get('id'),"El contenedor no cumple con los requisitos de peso y tampoco con los requisitos de seguridad", "RECHAZADO")
        else:
            contenedores_rechazados.append(i)
            generar_log(i.get('id'),"Hubo un problema para obtener los datos de este item del manifiesto", "RECHAZADO")
    print("\n")

contenedores_aprobados = list()
contenedores_rechazados = list()
manifiesto_carga = [
    {"id": "CONT-001", "peso": 18500, "tipo": "Standard", "destino": "China", "peligroso": False},
    {"id": "CONT-002", "peso": 22000, "tipo": "Reefer", "destino": "USA", "peligroso": False}, # Exceso de peso
    {"id": "CONT-003", "peso": 15000, "tipo": "Standard", "destino": "España", "peligroso": True}, # Requiere permiso
    {"id": "CONT-004", "peso": "12000", "tipo": "Standard", "destino": "China", "peligroso": False}, # Error de tipo de dato (string)
    {"id": "CONT-005", "peso": 5000, "tipo": "Flat Rack", "destino": "Japón", "peligroso": False},
    {"id": "CONT-006", "tipo": "Standard", "destino": "Brasil"} # Falta la llave 'peso' y 'peligroso'
]

procesar_manifiesto(manifiesto_carga, contenedores_aprobados, contenedores_rechazados)

for i in contenedores_aprobados:
    print(i['id'])
print("\n")

for i in contenedores_rechazados:
    print(i['id'])
print("\n")

num_rechazados = len(contenedores_rechazados)
num_aprobados = len(contenedores_aprobados)
num_procesados = len(contenedores_aprobados) + len(contenedores_rechazados)
print(f"Total Procesados: {num_procesados} | Aprobados: {num_aprobados} | Fallidos: {num_rechazados}")
    
    
    
    
    
    