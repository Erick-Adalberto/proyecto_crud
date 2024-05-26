
import tkinter as tk


#Importar los módulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox


class FormularioClientes:

    def Formulario():
        try:
            base = Tk()
            base.geometry("1200x600")
            base.title("MAESTRO DE CLIENTES")

        

            groupbox = LabelFrame(base,text="Datos del Cliente", padx=5,pady=5)
            groupbox.grid(row=0,column=0,padx=10,pady=10)
            
            def limitar_caracteres(event):
                if len(texBoxId.get()) >= 3:
                    texBoxId.delete(3, 'end')

                max_caracteres = 3  # Número máximo de caracteres permitidos

                groupbox = Label(base)
                groupbox.pack()

            labelId=Label(groupbox,text="Código:",width=13,font=("arial",10)).grid(row=0,column=0)
            texBoxId= Entry(groupbox)
            texBoxId.grid(row=0,column=1, sticky=W)
            texBoxId.bind('<KeyPress>', limitar_caracteres)

            labelRazonSocial=Label(groupbox,text="Razón Social:",width=13,font=("arial",10)).grid(row=0,column=2)
            texBoxRazonSocial= Entry(groupbox,width=57)
            texBoxRazonSocial.grid(row=0,column=3,)

            labelNombre=Label(groupbox,text="Nombre:",width=13,font=("arial",10)).grid(row=1,column=0)
            texBoxNombre= Entry(groupbox,width=100)
            texBoxNombre.grid(row=1,column=1, sticky=W)

            labelDireccion=Label(groupbox,text="Dirección:",width=13,font=("arial",10)).grid(row=2,column=0)
            texBoxDireccion= Entry(groupbox,width=100)
            texBoxDireccion.grid(row=2,column=1, sticky=W)

            labelGiro=Label(groupbox,text="Giro:", fg="gray",width=13,font=("arial",10)).grid(row=3,column=0)
            texBoxGiro= Entry(groupbox,width=100)
            texBoxGiro.grid(row=3,column=1)

            labelDepto=Label(groupbox,text="Depto:",width=13,font=("arial",10)).grid(row=4,column=0)
            texBoxDepto= Entry(groupbox,width=50)
            texBoxDepto.grid(row=4,column=1, sticky=W)

            labelMunicipio=Label(groupbox,text="Municipio:",width=13,font=("arial",10)).grid(row=5,column=0)
            texBoxMunicipio= Entry(groupbox,width=50)
            texBoxMunicipio.grid(row=5,column=1, sticky=W)

            labelVendedor=Label(groupbox,text="Vendedor:",width=13,font=("arial",10)).grid(row=6,column=0)
            texBoxVendedor= Entry(groupbox,width=100)
            texBoxVendedor.grid(row=6,column=1, sticky=W)

            labelNit=Label(groupbox,text="NIT ó DUI:",width=13,font=("arial",10)).grid(row=7,column=0)
            texBoxNit= Entry(groupbox,width=50)
            texBoxNit.grid(row=7,column=1, sticky=W)

            labelContribuyente=Label(groupbox,text="Tipo de Contribuyente:",width=20,font=("arial",10)).grid(row=7,column=2)
            seleccionContribuyente = tk.StringVar()
            combo = ttk.Combobox(groupbox,values=["PEQUEÑO","GRANDE","OTRO"], textvariable=seleccionContribuyente)
            combo.grid(row=7,column=3, sticky=W)

            labelRegistro=Label(groupbox,text="Registro:",width=13,font=("arial",10)).grid(row=8,column=0)
            texBoxRegistro= Entry(groupbox,width=50)
            texBoxRegistro.grid(row=8,column=1, sticky=W)

            labelPersona=Label(groupbox,text="Tipo de Persona:",width=20,font=("arial",10)).grid(row=8,column=2)
            seleccionPersona = tk.StringVar()
            combo = ttk.Combobox(groupbox,values=["NATURAL","JURIDICA"], textvariable=seleccionPersona)
            combo.grid(row=8,column=3, sticky=W)

            labelTel=Label(groupbox,text="Teléfono:",width=13,font=("arial",10)).grid(row=1,column=2)
            texBoxTel= Entry(groupbox,width=25)
            texBoxTel.grid(row=1,column=3, sticky=W)

            labelLimite=Label(groupbox,text="Limite:",width=13,font=("arial",10)).grid(row=9,column=0)
            texBoxLimite= Entry(groupbox,width=25)
            texBoxLimite.grid(row=9,column=1, sticky=W)

            labelPlazo=Label(groupbox,text="Plazo en días:",width=13,font=("arial",10)).grid(row=9,column=2)
            texBoxPlazo= Entry(groupbox,width=23)
            texBoxPlazo.grid(row=9,column=3, sticky=W)

            labelContacto=Label(groupbox,text="Contacto:",width=13,font=("arial",10)).grid(row=10,column=0)
            texBoxContacto= Entry(groupbox,width=100)
            texBoxContacto.grid(row=10,column=1, sticky=W)

            labelObservaciones=Label(groupbox,text="Observaciones:",width=13,font=("arial",10)).grid(row=11,column=0)
            texBoxObservaciones= Entry(groupbox,width=100)
            texBoxObservaciones.grid(row=11,column=1, sticky=W)

            base.mainloop()


        except ValueError as error:
                print("Error al mostrar la interfaz, error: {}".format(error))

    Formulario()
            