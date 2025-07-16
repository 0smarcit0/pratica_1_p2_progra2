import dijkstra
def menu():
    r = 1
    lista_nodos=dijkstra.cargardatos()
    IDs = set()
    for x in lista_nodos:
        if x.getvalor() not in IDs:
            IDs.add(x.getvalor())
    while r != 3:
        print("\t=====================")
        print("\tSistema transporte urbano")
        print("\t=====================")
        print("Seleccione una opcion \n\t1)Mostrar rutas asociadas directamente\n\t2)Obtener ruta mas corta\n\t3)Salir\n")
        r = int(input("Opcion: "))
        
        if r == 3:
            print("Hasta Luego!")
        elif r ==1:
            dijkstra.mostrar_red(lista_nodos)
            input("Presione cualquier tecla para continuar")
        elif r == 2:
            band1 = False
            start =0
            end =0
            while band1 == False:
                try:
                    start = int(input("Ingrese el id de la estacion de salida: "))
                    if start in IDs:
                        break
                    else:
                        print("\nError, el ID que ha ingresado no se encuentra registrado")
                except ValueError:
                    print("Error, entrada no valida")
            
            while band1 == False:
                try:
                    end = int(input("Ingrese el id de la estacion de llegada: "))
                    if end in IDs:
                        break
                    else:
                        print("\nError, el ID que ha ingresado no se encuentra registrado")
                except ValueError:
                    print("Error, entrada no valida")
            dijkstra.dijkstra(lista_nodos,start,end)
            for x in lista_nodos:
                x.setdist(99999)
                x.setexplorado(False)
            input("Presione cualquier tecla para continuar")
            
        