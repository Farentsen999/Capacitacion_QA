pedidos = [
    {"id": 101, "cliente": "Matias", "monto": 15500, "comuna": "Hualpén", "entregado": True},
    {"id": 102, "cliente": "Carla", "monto": -500, "comuna": "Hualpén", "entregado": False}, # BUG: Monto negativo
    {"id": 103, "cliente": "Luis", "monto": 25000, "comuna": "Concepción", "entregado": True},
    {"id": 104, "monto": 8000, "comuna": "Hualpén", "entregado": True}, # BUG: Falta la llave "cliente"
    {"id": 105, "cliente": "Ana", "monto": 45000, "comuna": "Hualpén", "entregado": False}
]

pedidos_hualpen_pendientes = list()
num_fallidos = 0

for i in range(5): # MEJORA: Usar for i in pedidos
    print(f"Procesando pedido {pedidos[i]["id"]}")
    if pedidos[i]["monto"] < 0:
        num_fallidos = num_fallidos + 1
        #MEJORA: usar '' en vez de "" para ['id'] o similar al usar f string
        print(f"[ERROR] Pedido {pedidos[i]["id"]} tiene un monto inválido")  
    try:
        print(f"El nombre del cliente asosiado al pedido {pedidos[i]["id"]} es {pedidos[i]["cliente"]}")
    # MEJORA: usar except KeyError para capturar el error especifico
    except:
        num_fallidos = num_fallidos + 1
        print("[CRÍTICO] Pedido #[id] no registra nombre de cliente")
    if pedidos[i]["comuna"] == "Hualpén" and pedidos[i]["entregado"] == False:
        pedidos_hualpen_pendientes.append(pedidos[i])
    print("\n")

print("CONCLUSIONES:")
print(f"El número de pedidos fallidos es {num_fallidos} y el número de pedidos pendientes es {len(pedidos_hualpen_pendientes)}")
