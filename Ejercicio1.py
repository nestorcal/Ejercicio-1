"""
========================================
Lista de Productos:
========================================
1 	 Pantalones	 200.0 	 50
2 	 Camisas 	 120.0 	 45
3 	 Corbatas 	 50.0 	 30
4 	 Casacas 	 350.0 	 15
========================================
[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir
Elija opción:

"""
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

def listarProductos(dic1,dic2,dic3):
    encabezado="""========================================
Lista de Productos:
========================================"""
    print(encabezado)
    for i in dic1:
        print("{0} \t {1} \t {2} \t {3}".format(i,dic1[i],dic2[i],dic3[i]))
    print("========================================")

while True:
    listarProductos(Productos,Precios,Stock)
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    opcion=input("Elija opción:")
    try:
        opcionVal=int(opcion)
    except ValueError:
        print("Introduzca valor correcto:")
