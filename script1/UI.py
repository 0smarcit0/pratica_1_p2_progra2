import back as b
import customtkinter as cus
from tkinter import * 
class App(cus.CTk):
    def __init__(self):
        super().__init__()
        #configuracion de la ventana:
        self.geometry("500x400")
        self.title("Aplicacion")
        
        #declaracion de widgets:
        #titulo principal
        self.titulo = cus.CTkLabel(self,text="Deteccion de minas subterraneas",font=("Corbel",21))
        self.titulo.place(x=100,y=20)
        
        #input con label identificador
        self.subtitulo1 = cus.CTkLabel(self,width=100,height=70,text="Mapa digitalizado", font=("Corbel",18))
        self.subtitulo1.place(x=25,y=50)
        self.entrada = cus.CTkTextbox(self,width=200,height=200)
        self.entrada.place(x=25,y=110)
        
        #output con label identificador
        self.subtitulo2 = cus.CTkLabel(self,width=100,height=70,text="Minas encontradas", font=("Corbel",18))
        self.subtitulo2.place(x=250,y=50)
        self.salida = cus.CTkTextbox(self,width=200,height=200)
        self.salida.place(x=250,y=110)
        
        #boton para procesar
        self.boton = cus.CTkButton(self,width=80,height=40,command=self.procesar,text="Procesar",font=("Corbel",19))
        self.boton.place(x=193,y=335)
        
        #nota especial
        self.nota = cus.CTkLabel(self,width=100,height=40,text="Nota: en la salida, sume 1 a la columna\n donde esta ubicado el *",font=("Corbel",12))
        self.nota.place(x=280,y=335)
        #se carga la data guardada en minas.in para posteriormente ponerla en el input
        try:
            with open('script1/minas.in') as file:
                self.entrada.insert("1.0",file.read())
        except FileNotFoundError:
            print("Hay un error con el archivo, porfavor vuelva a intentarlo")
    
    #funcion para procesar el input:
    def procesar(self):
        #se extrae el contenido del input 
        datatxt = self.entrada.get("1.0","end")
        #se divide el contenido del input en filas y se guarda en una lista
        data = datatxt.split("\n")
        #se procesa la lista para buscar minas (ver el archivo back.py para la logica de obtencion)
        procesado =b.getminas(data)
        #una vez procesado se inserta el resultado en el output
        self.salida.delete("1.0","end")
       
        self.salida.insert("1.0",procesado)