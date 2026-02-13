import json

class AuditorQA:  
    def __init__(self):
        self.registros_validos = []
        self.registros_rechazados = []      
    
    def validar_monto(self, monto):
        try:
            return int(float(monto)) if monto is not None else 0
        except (ValueError, TypeError):
            return 0
        
    def detectar_datos_faltantes(self, diccionario):
        lista_faltantes = []
        if "id" not in diccionario:
            lista_faltantes.append("el registro esta corrupto")
        if "monto" not in diccionario:
            lista_faltantes.append("el registro no tiene monto asignado")
        if "comuna" not in diccionario:
            lista_faltantes.append("el registro no tiene comuna asignada")
        if "cliente" not in diccionario:
            lista_faltantes.append("cliente desconocido")
        return lista_faltantes
    
    def cargar_datos(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lista_datos = json.load(archivo)
            return lista_datos

        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            return []
        except json.JSONDecodeError:
            print(f"Error: El archivo '{nombre_archivo}' tiene un formato JSON inválido (checkea comas o corchetes).")
            return []  
    
    def guardar_resultados(self, nombre_lista):
        try:
            with open('reporte_final.json', 'w', encoding='utf-8') as archivo:
                json.dump(nombre_lista, archivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
        
    def procesar_reporte(self, reporte_json):
        reporte_cargado = self.cargar_datos(reporte_json)
        if reporte_cargado != []:
            for i in reporte_cargado:
                datos_faltantes = self.detectar_datos_faltantes(i)
                if self.validar_monto(i.get("monto"))> 50000:
                    i["Prioridad"] = "Alta"
                if datos_faltantes != [] and datos_faltantes[0] != "cliente desconcido" and len(datos_faltantes) == 1:
                    i["MOTIVO DE FALLO: "] = datos_faltantes
                    self.registros_rechazados.append(i)                    
                else:
                    if datos_faltantes == ["cliente desconocido"]:
                        i["cliente"] = datos_faltantes[0]
                    self.registros_validos.append(i)
        total_registros = self.registros_validos + self.registros_rechazados
        resumen_estadistico = {"Total procesados":f"{len(total_registros)}", "Total aceptados" :f"{len(self.registros_validos)}", "Total rechazados":f"{len(self.registros_rechazados)}"}
        total_registros.append(resumen_estadistico)
        self.guardar_resultados(total_registros)
        

auditor = AuditorQA()
auditor.procesar_reporte('datos_auditoria.json')
                    
    
    

    
