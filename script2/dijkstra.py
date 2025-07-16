from nodo import Nodo  
import math

def getruta(nodo:Nodo):
    nodo.saludo()
    #caso base, cuando ya llega a la fuente y no hay mas predecesores:
    if nodo.getprev() == None:
        return 0
    #caso contrario, sigue con el predecesor para mostrarlo por pantalla
    else:
        return getruta(nodo.getprev())
    


#metodo de ordenamiento shell para ordenar la lista de prioridad
def shell(lista,n):
    if n<2:
        return lista[0]
    salto = math.floor(n/2)
    while salto >0:
        i = salto
        while i<n:
            
            temp = lista[i]
            j = i
            while j>=salto and lista[j-salto].getdistancia()>temp.getdistancia():
                lista[j] = lista[j-salto]
                j-=salto
            lista[j] = temp
            i = i+1
        
        salto = math.floor(salto/2)
    try:
        return lista[0]
    except IndexError:
        lista.append(0)
        return lista[0]
        
    


def dijkstra(lista,id_inicio, id_final):
    
    i = 0
    pos_idf = 0
    band1 = False
    band2 = False
    peso = 0
    lista_prioridad = []
    #seteo del nodo fuente y obtencion de la posicion del nodo final en la lista de nodos
    if id_inicio == id_final:
        print("Para llegar a un nodo desde el mismo hay un coste de 0")
        return 0
    while i<len(lista):
        if id_inicio == lista[i].getvalor():
            lista[i].setdist(0)
            lista[i].setprev(None)
            lista_prioridad.append(lista[i])
            band1 = True
        if id_final == lista[i].getvalor():
            pos_idf = i
            band2 = True
        if band1 and band2:
            break
        i = i+1
    #print("el nodo final es: ")
    #lista[pos_idf].saludo()
    
    while lista[pos_idf].getexplorado() == False:
        
        #se selecciona el nodo con el menor peso acomulado para explorar
        seleccionado = shell(lista_prioridad,len(lista_prioridad))
        if type(seleccionado) == int:
            break
        
        #como ya lo vamos a estudiar lo sacamos de la lista de prioridad
        lista_prioridad.pop(0)
        #se busca en la lista al nodo adyacente o al seleccionado con el menor peso en su camino
        for j in range(len(lista)):
            if seleccionado.getvalor() == lista[j].getvalor():
                #print(f"estado del nodo seleccionado (explorado o no) {lista[j].getexplorado()}")
                #lista[j].saludo()
                lista[j].setexplorado(True)
                i = j
                
        #una vez seleccionado el nodo se analizan sus adyacentes

        #print("===nodo seleccionado y sus adyacentes: ===")
        #lista[i].saludo()
        #print(lista[i].getcantady())
        
        for j in range(lista[i].getcantady()):
            dic = lista[i].getady(j) #se obtiene el diccionarico con id del nodo ady y el peso del camino hacia este
            #print(dic)
            for k in dic.keys():
                #print("id del adyacente:")
                for l in lista:
                    if l.getvalor() == k:
                        #se determina una nueva estimacion para el nodo, si la estimacion es menor a la que ya tenia,
                        #esta cambia por la nueva estimacion y se actualiza el predecesor de ese nodo
                        if lista[i].getdistancia() + dic.get(k) < l.getdistancia():
                            existe = False
                            #print("hay una mejor estimacion")
                            #print(f"nueva estimacion: {lista[i].getdistancia() + dic.get(k)}")
                            #print(f"estimacion anterior: {l.getdistancia()}")
                            
                            l.setdist(lista[i].getdistancia() + dic.get(k))
                            l.setprev(lista[i])
                            #print(l.getdistancia())
                            
                            
                            #se busca el nodo en la lista de prioridad para actualizar su peso, de encontrarse,
                            #se agrega a la lista
                            for x in range(len(lista_prioridad)):
                                if lista_prioridad[x].getvalor() == l.getvalor():
                                    lista_prioridad[x].setdist(l.getdistancia())
                                    existe = True
                                    break
                            if existe == False:
                                lista_prioridad.append(l)
        #cuando ya se encuentra el camino hacia el nodo objetivo, se imprime y se acaba el algoritmo
        if lista[pos_idf].getexplorado()==True:
            print("\nRuta minima encontrada: ")
            getruta(lista[pos_idf])
        #si la lista queda vacia, entonces no hay camino
        elif len(lista_prioridad) <1:
            print("no hay camino")
            return 0
    #se muestra el peso
    
    peso = lista[i].getdistancia()
    print(f"El peso de esta ruta es de: {peso}")


#lectura de datos y configuracion de la lista de adyacencia

def cargardatos():
    
    try:
        with open('./script2/red_transporte.txt') as file:
            ent = file.read().split("\n")
    except FileNotFoundError:
        print("Hay un error con el archivo, porfavor vuelva a intentarlo")
    
    #print(ent)
    n = ent[0].split(" ")
    n_nodos = int(n[0])
    #print(n_nodos)
    ids  = set()
    lista_nodos = []
    j = 0
    for i in range(int(n[1])):
        data = ent[i+1].split(" ")
        if int(data[0]) in ids:
            while j<len(lista_nodos):
                if int(data[0]) == lista_nodos[j].getvalor():
                    dic = {int(data[1]):int(data[2])}
                    lista_nodos[j].agregar_ady(dic)
                    break
                j = j+1
            j = 0
        else:
            ids.add(int(data[0]))
            nodo = Nodo(int(data[0]))
            if int(data[1])==0 and int(data[2])==0:
                pass
            else:
                dic = {int(data[1]):int(data[2])}
                nodo.agregar_ady(dic)
            lista_nodos.append(nodo)
    return lista_nodos

def mostrar_red(lista_nodos):
    for i in lista_nodos:
        print(f"\nConexiones directas desde la Estacion\parada: {i.getvalor()}")
        if i.getcantady() < 1:
            print("\tNo hay conexiones directas desde esta Estacion/parada")
        for j in range(i.getcantady()):
            dic = i.getady(j)
            for k in dic.keys():
                print(f"\tEstacion/parada: {k}")
lista_nodos = cargardatos()


