from tkinter import Tk, PhotoImage, Label
# from tkinter import PhotoImage

app = Tk()
app.title("Hola S.O")

# Lees la imagen:
# He colocado ruta relativa, es decir, la imagen a la misma 
# altura de la aplicación. Si prefieres, puedes colocar una
# ruta absoluta.
imagen = PhotoImage(file = "ejemplo.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen S.O de fondo")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Por defecto el fondo es blaco. Accediendo al método config
# de Label podrías, por ejemplo, establecer un color de fondo distinto:
# background.config(bg = "gray")

app.mainloop()