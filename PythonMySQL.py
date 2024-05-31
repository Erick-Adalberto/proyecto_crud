
import tkinter as tk


#Importar los módulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage


class FormularioClientes:

    def Formulario():
        try:
            base = Tk()
        
            base.geometry("918x600")
            base.resizable(0,0)
            base.title("MAESTRO DE CLIENTES")
            wtotal = base.winfo_screenwidth()
            htotal = base.winfo_screenheight()
            
            wventana = 918
            hventana = 600

            pwidth = round(wtotal/2-wventana/2)
            pheight = round(htotal/2-hventana/2)

            base.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

            groupbox = LabelFrame(base,text="Datos del Cliente", padx=5,pady=5, fg="black", bg="lightskyblue",)
            groupbox.grid(row=0,column=0,padx=10,pady=10)

            labelId=Label(groupbox,text="Código:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=0,column=0)
            texBoxId= Entry(groupbox, width=6)
            texBoxId.grid(row=0,column=1, sticky=W)

            labelCliente=Label(groupbox,text="Cliente:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=1,column=0)
            texBoxCliente= Entry(groupbox,width=75)
            texBoxCliente.grid(row=1,column=1, sticky=W)

            labelRazonSocial=Label(groupbox,text="Razón Social:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=2,column=0)
            texBoxRazonSocial= Entry(groupbox,width=57)
            texBoxRazonSocial.grid(row=2,column=1, sticky=W)

            labelDireccion=Label(groupbox,text="Dirección:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=3,column=0)
            texBoxDireccion= Entry(groupbox,width=75)
            texBoxDireccion.grid(row=3,column=1, sticky=W)

            labelGiro=Label(groupbox,text="Giro:", fg="black",width=13, bg="lightskyblue", font=("arial",10)).grid(row=4,column=0)
            texBoxGiro= Entry(groupbox,width=75)
            texBoxGiro.grid(row=4,column=1)

            labelDepto=Label(groupbox,text="Depto:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=5,column=0)
            texBoxDepto= Entry(groupbox,width=50)
            texBoxDepto.grid(row=5,column=1, sticky=W)

            labelMunicipio=Label(groupbox,text="Municipio:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=6,column=0)
            texBoxMunicipio= Entry(groupbox,width=50)
            texBoxMunicipio.grid(row=6,column=1, sticky=W)

            labelVendedor=Label(groupbox,text="Vendedor:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=7,column=0)
            texBoxVendedor= Entry(groupbox,width=75)
            texBoxVendedor.grid(row=7,column=1, sticky=W)

            labelNit=Label(groupbox,text="NIT ó DUI:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=8,column=0)
            texBoxNit= Entry(groupbox,width=50)
            texBoxNit.grid(row=8,column=1, sticky=W)

            labelContribuyente=Label(groupbox,text="Tipo de Contribuyente:",width=20, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=9,column=2)
            seleccionContribuyente = tk.StringVar()
            combo = ttk.Combobox(groupbox,values=["PEQUEÑO","GRANDE","OTRO"], textvariable=seleccionContribuyente)
            combo.grid(row=9,column=3, sticky=W)

            labelRegistro=Label(groupbox,text="Registro:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=9,column=0)
            texBoxRegistro= Entry(groupbox,width=50)
            texBoxRegistro.grid(row=9,column=1, sticky=W)

            labelPersona=Label(groupbox,text="Tipo de Persona:",width=20, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=10,column=2)
            seleccionPersona = tk.StringVar()
            combo = ttk.Combobox(groupbox,values=["NATURAL","JURIDICA"], textvariable=seleccionPersona)
            combo.grid(row=10,column=3, sticky=W)

            labelTel=Label(groupbox,text="Teléfono:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=1,column=2)
            texBoxTel= Entry(groupbox,width=25)
            texBoxTel.grid(row=1,column=3, sticky=W)

            labelWhatsapp=Label(groupbox,text="Whatsapp:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=2,column=2)
            texBoxWhatsapp= Entry(groupbox,width=25)
            texBoxWhatsapp.grid(row=2,column=3, sticky=W)

            labelEmail=Label(groupbox,text="E-mail:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=3,column=2)
            texBoxEmail= Entry(groupbox,width=25)
            texBoxEmail.grid(row=3,column=3, sticky=W)

            labelContacto=Label(groupbox,text="Contacto:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=10,column=0)
            texBoxContacto= Entry(groupbox,width=75)
            texBoxContacto.grid(row=10,column=1, sticky=W)

            labelObservaciones=Label(groupbox,text="Observaciones:",width=13, fg="black", bg="lightskyblue", font=("arial",10)).grid(row=11,column=0)
            texBoxObservaciones= Entry(groupbox,width=75)
            texBoxObservaciones.grid(row=11,column=1, sticky=W)

            Button(groupbox,text="Guardar",width=10).grid(row=13,column=1,sticky="e")
            Button(groupbox,text="Modificar",width=10).grid(row=13,column=2)
            Button(groupbox,text="Eliminar",width=10).grid(row=13,column=3, sticky=W)

            groupbox = LabelFrame(base,text="Lista de Clientes",padx=5,pady=5,)
            groupbox.grid(row=14,column=0,padx=5,pady=5)

            #Crear un Treeview

            #Configurar las columnas

            tree = ttk.Treeview(groupbox,columns=("Id","Cliente","Telefono","Razon Social"),show='headings',height=5)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="Codigo")

            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="Cliente")

            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="Razon Social")

            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="Telefono")

            

            tree.pack()

            base.mainloop()


        except ValueError as error:
                print("Error al mostrar la interfaz, error: {}".format(error))

    Formulario()
            