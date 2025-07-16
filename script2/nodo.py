class Nodo():
    def __init__(self,valor):
        self.valor = valor
        self.nodo_ant = None
        self.explorado = False
        self.dist_r = 99999
        self.list_ady = []
    
    def setdist(self,dist):
        self.dist_r = dist
    def setprev(self,nodo_prev):
        self.nodo_ant = nodo_prev
        
    def setexplorado(self,bool):
        self.explorado = bool
    
    
   
    def getvalor(self):
        return self.valor
    def getlista(self):
        return self.list_ady
    def getexplorado(self):
        return self.explorado
    def getdistancia(self):
        return self.dist_r
    def getcantady(self):
        return len(self.list_ady)
    def getady(self,pos):
        return self.list_ady[pos]    
    
    def getprev(self):
        return self.nodo_ant
    
    def saludo(self):
        print(f"Estacion/parada con ID: {self.valor}")
    def agregar_ady(self,ady):
        self.list_ady.append(ady)



