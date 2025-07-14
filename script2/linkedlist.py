from nodo import Nodo  
import math

def getruta(nodo):
    nodo.saludo()
    if nodo.getprev() == None:
        return 0
    else:
        return getruta(nodo.getprev())
    
def getnoexplorados(lista):
    inexplorados = []
    for x in lista:
        if x.getexplorado() == False:
            inexplorados.append(x)
    return inexplorados

def shell(lista,n):
    
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
    
    return lista[0]


def dijkstra(lista,id_inicio, id_final):
    i = 0
    pos_idf = 0
    pos_idi = 0
    band1 = False
    band2 = False
    peso = 0
    lista2 = lista.copy()
    camino =[]
    
    #seteo del nodo fuente y obtencion de la posicion del nodo final en la lista de nodos
    while i<len(lista):
        if id_inicio == lista[i].getvalor():
            lista[i].setdist(0)
            lista[i].setprev(None)
            band1 = True
        if id_final == lista[i].getvalor():
            pos_idf = i
            band2 = True
        if band1 and band2:
            break
        i = i+1
    print("el nodo final es: ")
    lista[pos_idf].saludo()
    
    
    
    while lista[pos_idf].getexplorado() == False:
        
        #bajo prueba, se supone que cuando se consiga un poso, vuelva al nodo fuente y busque otro camino
        if len(lista2) < 1:
            seleccionado = lista[pos_idi]
            #lis
            print("ya no hay mas joven")
        else:
            #esto ya pasa si el nodo si tiene adyacentes
            listaAux = getnoexplorados(lista2)
            seleccionado = shell(listaAux,len(listaAux))
        
        #se busca en la lista al nodo adyacente o al seleccionado con el menor peso en su camino
        for j in range(len(lista)):
            if seleccionado.getvalor() == lista[j].getvalor():
                print(f"estado del nodo seleccionado (explorado o no) {lista[j].getexplorado()}")
                lista[j].saludo()
                
                camino.append(lista[j])
                lista[j].setexplorado(True)
                i = j
                
        #una vez seleccionado el nodo se analizan sus adyacentes

        print("===nodo seleccionado y sus adyacentes: ===")
        lista[i].saludo()
        print(lista[i].getcantady())
        
        lista2.clear()
        for j in range(lista[i].getcantady()):
            dic = lista[i].getady(j) #se obtiene el diccionarico con id del nodo ady y el peso del camino hacia este
            print(dic)
            for k in dic.keys():
                print("id del adyacente:")
                for l in lista:
                    if l.getvalor() == k:
                        #se determina una nueva estimacion para el nodo, si la estimacion es menor a la que ya tenia,
                        #esta cambia por la nueva estimacion y se actualiza el predecesor de ese nodo
                        if lista[i].getdistancia() + dic.get(k) < l.getdistancia():
                
                            print("hay una mejor estimacion")
                            print(f"nueva estimacion: {lista[i].getdistancia() + dic.get(k)}")
                            print(f"estimacion anterior: {l.getdistancia()}")
                            
                            l.setdist(lista[i].getdistancia() + dic.get(k))
                            
                            l.setprev(lista[i])
                            print(l.getdistancia())
                        lista2.append(l)
                            
        #lista[pos_idi].setprev(None)
        #mostrar ruta
        if lista[pos_idf].getexplorado()==True:
            getruta(lista[pos_idf])
                    
    peso = lista[i].getdistancia()
    print(peso)
    return camino


#lectura de datos y configuracion de la lista de adyacencia
try:
    with open('red_transporte.txt') as file:
        ent = file.read().split("\n")
except FileNotFoundError:
    print("Hay un error con el archivo, porfavor vuelva a intentarlo")
    
print(ent)
n = ent[0].split(" ")
n_nodos = int(n[0])
print(n_nodos)
ids  = set()
lista_nodos = []
j = 0
for i in range(int(n[1])):
    data = ent[i+1].split(" ")
    if int(data[0]) in ids:
        while j<len(lista_nodos):
            if int(data[0]) == lista_nodos[j].getvalor():
                #nodo = Nodo(int(data[1]))
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



print("--------")
camino = dijkstra(lista_nodos,2,8)
#print(lista_nodos)
#for x in lista_nodos:
 #   print(x.getlista())
