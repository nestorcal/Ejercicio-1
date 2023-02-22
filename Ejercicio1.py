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

def agregar(dic1,dic2,dic3):
    nuevoElementoIndice=max(dic1,key=int)+1
    nuevoValorPro=str(input("Ingrese Producto: "))
    nuevoValorPrecio=input("Ingrese Precio: ")
    try:
        dic2[nuevoElementoIndice]=float(nuevoValorPrecio)
        nuevoValorStock=input("Ingrese Stock: ")
        try:
            dic3[nuevoElementoIndice]=int(nuevoValorStock)
            dic1[nuevoElementoIndice]=nuevoValorPro
            print("Se agrego producto.")
        except ValueError:
            print("Ingrese Valor numerico")
    except ValueError:
        print("Ingrese Valor numerico")

def eliminar(dic1,dic2,dic3,indice):
    if indice in dic1:
        del(dic1[indice])
        del(dic2[indice])
        del(dic3[indice])
    else:
        print("**** Indice no existe ****")

def actualizar(dic1,dic2,dic3,indice):
    if indice in dic1:
        nuevoValorPro=str(input("Ingrese Producto: "))
        nuevoValorPrecio=input("Ingrese Precio: ")
        try:
            dic2[indice]=float(nuevoValorPrecio)
            nuevoValorStock=input("Ingrese Stock: ")
            try:
                dic3[indice]=int(nuevoValorStock)
                dic1[indice]=nuevoValorPro
                print("Se actualizó producto.")
            except ValueError:
                print("Ingrese Valor numerico")
        except ValueError:
            print("Ingrese Valor numerico")
    else:
        print("**** Indice no existe ****")

while True:
    listarProductos(Productos,Precios,Stock)
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    opcion=input("Elija opción:")
    try:
        opcionVal=int(opcion)
        if opcionVal==1:
            agregar(Productos,Precios,Stock)
        elif opcionVal==2:
            indiceEliminar=input("Ingrese indice de Elemento que desea eliminar: ")
            eliminar(Productos, Precios, Stock, int(indiceEliminar))
        elif opcionVal==3:
            indiceActualizar = input("Ingrese indice de Elemento que desea Actualizar: ")
            actualizar(Productos, Precios, Stock, int(indiceActualizar))
        elif opcionVal==4:
            break

    except ValueError:
        print("Introduzca valor correcto:")
