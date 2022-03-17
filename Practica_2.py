# -- Uso de ventanas
from tkinter import *
# -- Ventanas para mostrar mensajes emergentes
from tkinter import messagebox

# ------ Función para contar los espacios en blanco de un String


def contarEspacios():

    def contar():
        numEspacios = 0
        cadena = cadenaUsuario.get()
        for letra in cadena:
            if letra == ' ':
                numEspacios += 1
        messagebox.showinfo(message="La cadena tiene: " +
                            str(numEspacios) + " espacios en blanco", title=" Resultado")

    ventanaContarEspacio = Tk()
    ventanaContarEspacio.title(
        " Practica 2 Python | Contar espacios de una cadena")
    ventanaContarEspacio.iconbitmap("logo_py.ico")
    ventanaContarEspacio.resizable(0, 0)

    frameContarEspacio = Frame(
        ventanaContarEspacio, width=500, height=200, bg="white")
    frameContarEspacio.pack()

    Label(frameContarEspacio, text="Introduce una cadena: ",
          font=12, bg="white").grid(row=0, column=0, sticky="e", padx=10)

    cadenaUsuario = Entry(frameContarEspacio, width=50)
    cadenaUsuario.grid(row=0, column=1, padx=10, pady=20)

    Button(frameContarEspacio, width=20, text="Contar",
           command=contar).grid(row=1, columnspan=2, padx=10, pady=20)

    ventanaContarEspacio.mainloop()


# ------ Función para convertir en mayusculas o minisculas un char

def invertirLetra():

    def invertir():
        cadenaAux = str()
        cadena = cadenaUsuario.get()

        for letra in cadena:
            if ord(letra) >= 65 and ord(letra) <= 90:
                cadenaAux += chr(ord(letra) + 32)
            elif ord(letra) >= 97 and ord(letra) <= 122:
                cadenaAux += chr(ord(letra) - 32)
            else:
                cadenaAux += letra

        messagebox.showinfo(message="Cadena invertida: " +
                            cadenaAux, title=" Resultado")

    ventanaInvertir = Tk()
    ventanaInvertir.title(
        " Practica 2 Python | Invertir caracteres a minusculas o mayusculas")
    ventanaInvertir.iconbitmap("logo_py.ico")
    ventanaInvertir.resizable(0, 0)

    frameInvertir = Frame(
        ventanaInvertir, width=500, height=200, bg="white")
    frameInvertir.pack()

    Label(frameInvertir, text="Introduce una cadena: ",
          font=12, bg="white").grid(row=0, column=0, sticky="e", padx=10)

    cadenaUsuario = Entry(frameInvertir, width=50)
    cadenaUsuario.grid(row=0, column=1, padx=10, pady=20)

    Button(frameInvertir, width=20, text="Invertir",
           command=invertir).grid(row=1, columnspan=2, padx=10, pady=20)

    ventanaInvertir.mainloop()


# ------ Función para obtener una sub-cadena dado un delimitador

def obtenerSubCadena():

    def subCadena():
        cadenaAux = ""
        cadena = cadenaUsuario.get()
        demilitador = demilitadorUsuario.get()
        for letra in cadena:
            if letra == demilitador:
                break
            else:
                cadenaAux += letra

        messagebox.showinfo(message="La sub-cadena es: " +
                            cadenaAux, title=" Resultado")

    ventanaSubCadena = Tk()
    ventanaSubCadena.title(
        " Practica 2 Python | Obtener una Sub-Cadena")
    ventanaSubCadena.iconbitmap("logo_py.ico")
    ventanaSubCadena.resizable(0, 0)

    frameSubCadena = Frame(
        ventanaSubCadena, width=500, height=200, bg="white")
    frameSubCadena.pack()

    Label(frameSubCadena, text="Introduce una cadena: ",
          font=12, bg="white").grid(row=0, column=0, sticky="e", padx=10)

    cadenaUsuario = Entry(frameSubCadena, width=50)
    cadenaUsuario.grid(row=0, column=1, padx=10, pady=20)

    Label(frameSubCadena, text="Introduce un demilitador: ",
          font=12, bg="white").grid(row=1, column=0, sticky="e", padx=10)

    demilitadorUsuario = Entry(frameSubCadena, width=50)
    demilitadorUsuario.grid(row=1, column=1, padx=10, pady=20)

    Button(frameSubCadena, width=20, text="Obtener Sub-Cadena",
           command=subCadena).grid(row=2, columnspan=2, padx=10, pady=20)

    ventanaSubCadena.mainloop()


# ------ Creación de la ventana principal del programa
ventana = Tk()
ventana.title(" Practica 2 Python")
ventana.iconbitmap("logo_py.ico")
ventana.resizable(0, 0)

# ------ Frame o Panle principal. Se incluye dentro de la ventana principal
mainFrame = Frame(width=500, height=200, bg="white")
mainFrame.pack()

# ------ Creación de Etiquetas y Botones. Se incluyen dentro del Frame principal
Label(mainFrame, text="Seleccione una opción.",
      bg="white", font=12).place(x=150, y=10)

Button(mainFrame, text="Contar espacio",
       bg="white", font=12, command=contarEspacios).place(x=150, y=50)

Button(mainFrame, text="Invertir letras",
       bg="white", font=12, command=invertirLetra).place(x=150, y=100)

Button(mainFrame, text="Obtener sub-cadena",
       bg="white", font=12, command=obtenerSubCadena).place(x=150, y=150)


# ------ Función principal
def run():
    # --- La función "mainloop" sirve para ejecuta constantemente la ventana, hasta presionar [X]
    ventana.mainloop()
    print("ajshdkjhaskjd")


if __name__ == "__main__":
    run()
