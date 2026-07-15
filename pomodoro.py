# Pomodoro Timer
# Lo que se busca con esta app es una app de escritorio pomodoro la cual cuente con una interfaz grafica por medio de TKinter
# Usara unos cuantos botones para iniciar, pausar y reiniciar el temporizador, y mostrara el tiempo restante en pantalla.
# No se puede modificar la cantidad de tiempo de trabajo y descanso de 5 minutos, pero se podra calcular la cantidad de ciclos
# El minimo sera de 25 min y 5 min de descanso solamente, pero se podra tener 4 sesiones de 25 con 3 breaks de 5 minutos y 15 minutos
# de ultimo break

import tkinter as tk
from tkinter import font
import time
import pygame

#Display de la ventana 
root = tk.Tk()
root.title("Pomodoro Goat")
root.resizable(False, False)
root.configure(bg="#b1fcbb")

#Aca voy a centrar la ventana en la pantalla y darle el size de 300x400
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
x = (wtotal // 2) - (300 // 2)
y = (htotal // 2) - (400 // 2)
root.geometry(f"300x400+{x}+{y}")

#Texto que de ahi voy a modificar para que aparezca el nombre de la app y el autor
fuente_minecraft = font.Font(family="Minecraft Default", size=24)
etiqueta = tk.Label(root, text="Pomodoro Goat", font=fuente_minecraft, fg="black", bg="#b1fcbb")
etiqueta.pack(pady=35)

#Vamos a intentar colocar ahora las imagenes de pausa y continuar de al medio de de la pantalla y dejare comentado el de continuar mientras
idle = tk.PhotoImage(file="RalseiIDLE.gif")
#break = tk.PhotoImage(file="RalseiBreak.png") 
#focusing = tk.PhotoImage(file="RalseiFocusing.gif")

etiqueta = tk.Label(root, image=idle, bg="#b1fcbb")
etiqueta.pack()

#En esta parte siguiendo el orden de la app voy a colocar el temporizador en pantalla y lo voy a centrar
temporizador = tk.Label(root, text="25:00", font=("Minecraft Default", 48), fg="black", bg="#b1fcbb")
temporizador.pack(pady=20)


#Definir los 3 botones correspondientes a iniciar, pausar y reiniciar el temporizador 
def timerStart():
    print("Iniciando temporizador")
def timerPause():
    print("Pausando temporizador")
def timerReset():
    print("Reiniciando temporizador")

botonStart = tk.Button(root, text="Iniciar", font=("Minecraft Default", 11), command=timerStart, bg="#ff96f6")
botonStart.place(x=30, y=300, width=60, height=30)
botonPause = tk.Button(root, text="Pausar", font=("Minecraft Default", 11), command=timerPause, bg="#ff96f6")
botonPause.place(x=120, y=300, width=60, height=30)
botonReset = tk.Button(root, text="Reiniciar", font=("Minecraft Default", 11), command=timerReset, bg="#ff96f6")
botonReset.place(x=210, y=300, width=60, height=30)

#Definir cantidad de ciclos de estudio (entre 1 y 4)
def ciclosSeleccionados():
    verify = 0
    if ciclos.get() == "1":
        print("1")
        contadorPrint.config(text="1")
    elif ciclos.get() == "2":
        print("2")
        contadorPrint.config(text="2")
    elif ciclos.get() == "3":
        print("3")
        contadorPrint.config(text="3")
    elif ciclos.get() == "4":
        print("4")
        contadorPrint.config(text="4")
    
ciclos = tk.StringVar(value="1") 
tk.Radiobutton(root, command=ciclosSeleccionados, text="1", variable=ciclos, value="1", font=("Minecraft Default", 11), bg="#ff96f6").place(x=50, y=345, width=50, height=25)
tk.Radiobutton(root, command=ciclosSeleccionados, text="2", variable=ciclos, value="2", font=("Minecraft Default", 11), bg="#ff96f6").place(x=100, y=345, width=50, height=25)
tk.Radiobutton(root, command=ciclosSeleccionados, text="3", variable=ciclos, value="3", font=("Minecraft Default", 11), bg="#ff96f6").place(x=150, y=345, width=50, height=25)
tk.Radiobutton(root, command=ciclosSeleccionados, text="4", variable=ciclos, value="4", font=("Minecraft Default", 11), bg="#ff96f6").place(x=200, y=345, width=50, height=25)

contadorPrint = tk.Label(root, text="1", font=("Minecraft Default", 30), fg="black", bg="#b1fcbb")
contadorPrint.place(x=240, y=110, width=30, height=30)

root.mainloop()