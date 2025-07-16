global cant_ady
cant_ady = 0

#funcion donde se lleva acabo la busqueda de minas siguiendo los criterios
def getminas(data):
    nfc = data[0].split(" ") #numero de filas y columnas
    separado = [] #lista aux 
    vms = 0 #var para guardar el valor de la mina seleccionada (MD(i,j))
    
    posms = 0 #pos de la mina seleccionada
    posady = 0 #pos de las posibles minas adyacentes
    c = 0 #contador aux
    sumtop = 0
    sumbot = 0
    sumizde = 0
    prom=0
    encontradasx = []
    encontradasy = []
    global cant_ady
    #se separan las filas:
    for n in range(int(nfc[0])):
       separado.append(data[n+1].split(" "))
    print(separado)
    #ahora se analiza cada fila
    for n in separado:
        print(n)
        d = n
        #dentro de cada fila analizamos cada valor recogido
        for i in d:
            try:
                #obtenemos el valor MD(i,j)
                vms = int(i)
                print("vms: {} en la pos: {}".format(vms,posms))
            except ValueError:
                vms = 0
                
            #evaluamos si hay fila anterior a la que estamos
            if(eval_fila(c-1,separado)):
                print("fila de arriba: {}".format(separado[c-1]))
                posady = posms-1
                #se evaluan todos los adyacentes de esa fila
                for j in range(3):
                    sumtop = sumtop + eval_ady(posady,separado[c-1])
                    posady = posady+1
                posady = 0
            #evaluamos si hay fila siguiente
            if(eval_fila(c+1,separado)):
                print("fila de abajo: {}".format(separado[c+1]))
                posady = posms-1
                for j in range(3):
                    #se evaluan todos los adyacentes de esa fila
                    sumbot = sumbot + eval_ady(posady,separado[c+1])
                    posady = posady+1
                posady = 0
                
            posady = posms-1
            for j in range(2):
                #se evalua el lado izquierdo y derecho de la mina seleccionada
                sumizde = sumizde + eval_ady(posady,separado[c])
                posady = posady+2
            posady = 0
            
            if(cant_ady == 0):
                cant_ady = 1
            prom=(sumtop+sumizde+sumbot)/cant_ady
            posms = posms+1
            print("------------")
            print("vms: {}".format(vms))
            print("cant_ady: {}".format(cant_ady))
            print("sumtopt: {}".format(sumtop))
            print("sumbot: {}".format(sumbot))
            print("sumizde: {}".format(sumizde))
            if vms+prom >40:
                print("es una mina")
                encontradasx.append(posms)
                encontradasy.append(c+1)

            print("------------")
            sumtop = 0
            sumbot = 0
            sumizde = 0
            cant_ady = 0
       
        c = c+1
        posms =0
    print(encontradasx)
    print(encontradasy)
    
    return generar_salida(encontradasx,encontradasy,nfc[0],nfc[1]) 

#funcion para evaluar las lecturas adyadentes a MD(i,j)
def eval_ady(n,data):
    val = 0
    
    if n<0:
        return 0
    else:
        try:
            val= int(data[n])        
            print("valor a sumar: {}".format(val))
            global cant_ady 
            cant_ady = cant_ady+1
        except IndexError:
            print("el valor no existe")
        return val


#funcion para evaluar las filas adyacentes a la fila seleccionada 
def eval_fila(n,data):
    if n<0:
        return False
    else:
        try:
            val = data[n]
        except IndexError:
            print("la fila no existe")
            return False
    
    return True 


#funcion para generar la matriz de salida
def generar_salida(x,y,f,c):
    salida = ""
    index = 0
    #se crean las columnas
    for i in range(int(c)):
        salida = salida + " " + str(i+1)
    salida = salida +" \n"
    #se van agregando los * a donde corresponde
    for i in range(int(f)):
        salida = salida+str(i+1)
        for j in range(int(c)):
            if index >= len(x):
                break
            print(str(x[index])+" "+str(y[index]))
            if x[index] == j+1 and y[index] == i+1:
                salida = salida + "* "
                print(f"si es {index}, x:{j}, y:{i}")
                index = index +1
                
            else:
                salida = salida +"  "
        salida = salida+" \n"
    
    #se guarda el resultado en el archivo de salida
    try:
        with open('script1/minas.out',"w") as file:
            file.write(salida)
               
    except FileNotFoundError:
        print("Hay un error con el archivo, porfavor vuelva a intentarlo")
    
    print(salida)
    return salida