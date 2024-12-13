##vanessa abigail alvrado elizalde ##
#hacer un juego tradicional#
#piedra papel o tijera #
#con interfaz grafica  de preferencia que sea rosada 
import tkinter as tk
import random

class JuegoPiedraPapelTijera:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        
        # poniendo un color rosita pastel 
        self.root.configure(bg='pink')  ( pink rosado)
        
        # Inicializar puntuaciones
        self.puntuacion_jugador = 0
        self.puntuacion_computadora = 0
        
        # Crear elementos de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Título
        tk.Label(self.root, text="¡Piedra, Papel o Tijera!", font=("Arial", 24), bg='pink').pack(pady=10)

        # Botones para las opciones del jugador
        self.boton_piedra = tk.Button(self.root, text="Piedra", command=lambda: self.jugar("Piedra"), bg='lightpink')
        self.boton_piedra.pack(side=tk.LEFT, padx=10)

        self.boton_papel = tk.Button(self.root, text="Papel", command=lambda: self.jugar("Papel"), bg='lightpink')
        self.boton_papel.pack(side=tk.LEFT, padx=10)

        self.boton_tijera = tk.Button(self.root, text="Tijera", command=lambda: self.jugar("Tijera"), bg='lightpink')
        self.boton_tijera.pack(side=tk.LEFT, padx=10)

        ### mostrar el resultado
        self.resultado_texto = tk.StringVar()
        self.resultado_label = tk.Label(self.root, textvariable=self.resultado_texto, font=("Arial", 16), bg='pink')
        self.resultado_label.pack(pady=20)

        ##. mostrar la selección de la computadora
        self.seleccion_computadora_texto = tk.StringVar()
        self.seleccion_computadora_label = tk.Label(self.root, textvariable=self.seleccion_computadora_texto, font=("Arial", 16), bg='pink')
        self.seleccion_computadora_label.pack(pady=20)

        # contador de puntuación entre la persona o la computadora #######
        self.puntuacion_jugador_label = tk.Label(self.root, text=f"Puntuación Jugador: {self.puntuacion_jugador}", font=("Arial", 14), bg='pink')
        self.puntuacion_jugador_label.pack(pady=5)

        self.puntuacion_computadora_label = tk.Label(self.root, text=f"Puntuación Computadora: {self.puntuacion_computadora}", font=("Arial", 14), bg='pink')
        self.puntuacion_computadora_label.pack(pady=5)
        #aqui vamos a utilizar el def 
    def jugar(self, eleccion_jugador):
        ##claramente tenemos las opciones  
        opciones = ["Piedra", "Papel", "Tijera"] 
        eleccion_computadora = random.choice(opciones)
        self.seleccion_computadora_texto.set(f"Computadora eligió: {eleccion_computadora}")
        ##aui vamos a utilizar la bariable if y elif
        if eleccion_jugador == eleccion_computadora:
            self.resultado_texto.set("¡Empate!")
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra"):
            self.resultado_texto.set("¡Ganaste!") 
            self.puntuacion_jugador += 1
        else:
            self.resultado_texto.set("¡Perdiste!")
            self.puntuacion_computadora += 1
            #aqui te dira visualmente si ganastes o perdiste #

        # Actualizar las puntuaciones
        self.puntuacion_jugador_label.config(text=f"Puntuación Jugador: {self.puntuacion_jugador}")
        self.puntuacion_computadora_label.config(text=f"Puntuación Computadora: {self.puntuacion_computadora}")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoPiedraPapelTijera(root)#asignacion del juego #
    root.mainloop()
