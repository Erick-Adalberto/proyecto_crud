
import tkinter as tk


#Importar los módulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conexion import *


class FormularioClientes:

 global base
 base =None
 
 global texBoxId
 texBoxId =None

 global texBoxCliente
 texBoxCliente =None

 global texBoxRazonSocial
 texBoxRazonSocial =None

 global texBoxTel
 texBoxTel =None

 global texBoxWhatsapp
 texBoxWhatsapp =None

 global texBoxEmail
 texBoxEmail =None

 global texBoxDireccion
 texBoxDireccion =None

 global texBoxDepto
 texBoxDepto =None

 global texBoxDistrito
 texBoxDistrito =None

 global texBoxGiro
 texBoxGiro =None

 global texBoxVendedor
 texBoxVendedor =None

 global texBoxNit
 texBoxNit =None

 global texBoxRegistro
 texBoxRegistro =None

 global texBoxContacto
 texBoxContacto =None

 global comboContribuyente
 comboContribuyente =None

 global comboPersona
 comboPersona =None

 global texBoxObservaciones
 texBoxObservaciones =None

 global groupbox
 groupbox =None

 global tree
 tree =None


def Formulario():
        
        global base
        global texBoxId
        global texBoxCliente
        global texBoxRazonSocial
        global texBoxTel
        global texBoxWhatsapp
        global texBoxEmail
        global texBoxDireccion
        global texBoxDepto
        global texBoxDistrito
        global texBoxGiro
        global texBoxVendedor
        global texBoxNit
        global texBoxRegistro
        global texBoxContacto
        global comboContribuyente
        global comboPersona
        global texBoxObservaciones
        global groupbox
        global tree

        try:
            base = Tk()
        
            base.geometry("918x510")
            base.resizable(0,0)
            base.title("MAESTRO DE CLIENTES")
            
            imagen=PhotoImage(file="imagen.png")
            background=Label(image=imagen,text="Prueba de imagen")
            background.place(x=0,y=0, relwidth=1, relheight=1)
            
            wtotal = base.winfo_screenwidth()
            htotal = base.winfo_screenheight()
            
            wventana = 918
            hventana = 510

            pwidth = round(wtotal/2-wventana/2)
            pheight = round(htotal/2-hventana/2)

            base.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

            groupbox = LabelFrame(base,text="Datos del Cliente", padx=5,pady=5, fg="green2", bg="gray24",)
            groupbox.grid(row=0,column=0,padx=10,pady=10)

            labelId=Label(groupbox,text="Código:",width=14, fg="white", bg="gray24", font=("arial",10)).grid(row=0,column=0)
            texBoxId= Entry(groupbox, width=4)
            texBoxId.grid(row=0,column=1, sticky=W)

            labelCliente=Label(groupbox,text="Cliente:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=1,column=0)
            texBoxCliente= Entry(groupbox,width=75)
            texBoxCliente.grid(row=1,column=1, sticky=W)

            labelRazonSocial=Label(groupbox,text="Razón Social:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=2,column=0)
            texBoxRazonSocial= Entry(groupbox,width=57)
            texBoxRazonSocial.grid(row=2,column=1, sticky=W)

            labelTel=Label(groupbox,text="Teléfono:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=1,column=2)
            texBoxTel= Entry(groupbox,width=25)
            texBoxTel.grid(row=1,column=3, sticky=W)

            labelWhatsapp=Label(groupbox,text="Whatsapp:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=2,column=2)
            texBoxWhatsapp= Entry(groupbox,width=25)
            texBoxWhatsapp.grid(row=2,column=3, sticky=W)

            labelEmail=Label(groupbox,text="E-mail:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=3,column=2)
            texBoxEmail= Entry(groupbox,width=25)
            texBoxEmail.grid(row=3,column=3, sticky=W)

            labelDireccion=Label(groupbox,text="Dirección:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=3,column=0)
            texBoxDireccion= Entry(groupbox,width=75)
            texBoxDireccion.grid(row=3,column=1, sticky=W)

            labelDepto=Label(groupbox,text="Departamento:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=4,column=0)
            texBoxDepto= Entry(groupbox,width=50)
            texBoxDepto.grid(row=4,column=1, sticky=W)

            labelDistrito=Label(groupbox,text="Distrito:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=5,column=0)
            texBoxDistrito= Entry(groupbox,width=50)
            texBoxDistrito.grid(row=5,column=1, sticky=W)

            labelGiro=Label(groupbox,text="Giro:", fg="white",width=13, bg="gray24", font=("arial",10)).grid(row=6,column=0)
            texBoxGiro= Entry(groupbox,width=75)
            texBoxGiro.grid(row=6,column=1)

            labelVendedor=Label(groupbox,text="Vendedor:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=7,column=0)
            texBoxVendedor= Entry(groupbox,width=75)
            texBoxVendedor.grid(row=7,column=1, sticky=W)

            labelNit=Label(groupbox,text="NIT ó DUI:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=8,column=0)
            texBoxNit= Entry(groupbox,width=50)
            texBoxNit.grid(row=8,column=1, sticky=W)

            labelRegistro=Label(groupbox,text="Registro:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=9,column=0)
            texBoxRegistro= Entry(groupbox,width=50)
            texBoxRegistro.grid(row=9,column=1, sticky=W)

            labelContacto=Label(groupbox,text="Contacto:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=10,column=0)
            texBoxContacto= Entry(groupbox,width=75)
            texBoxContacto.grid(row=10,column=1, sticky=W)

            labelContribuyente=Label(groupbox,text="Tipo de Contribuyente:",width=20, fg="white", bg="gray24", font=("arial",10)).grid(row=9,column=2)
            seleccionContribuyente = tk.StringVar() 
            comboContribuyente = ttk.Combobox(groupbox,values=["PEQUEÑO","GRANDE","OTRO"], textvariable=seleccionContribuyente)
            comboContribuyente.grid(row=9,column=3, sticky=W)

            labelPersona=Label(groupbox,text="Tipo de Persona:",width=20, fg="white", bg="gray24", font=("arial",10)).grid(row=10,column=2)
            seleccionPersona = tk.StringVar()
            comboPersona = ttk.Combobox(groupbox,values=["NATURAL","JURIDICA"], textvariable=seleccionPersona)
            comboPersona.grid(row=10,column=3, sticky=W)

            labelObservaciones=Label(groupbox,text="Observaciones:",width=13, fg="white", bg="gray24", font=("arial",10)).grid(row=11,column=0)
            texBoxObservaciones= Entry(groupbox,width=75)
            texBoxObservaciones.grid(row=11,column=1, sticky=W)

            Button(groupbox,text="Guardar",width=10,command=guardarRegistro).grid(row=13,column=1,sticky="e")
            Button(groupbox,text="Modificar",width=10,command=modificarRegistro).grid(row=13,column=2)
            Button(groupbox,text="Eliminar",width=10,command=eliminarRegistro).grid(row=13,column=3, sticky=W)

            groupbox = LabelFrame(base,text="Lista de Clientes",padx=5,pady=5,fg="green2", bg="gray24",)
            groupbox.grid(row=14,column=0,padx=5,pady=5)

            #Crear un Treeview

            #Configurar las columnas

            tree = ttk.Treeview(groupbox,columns=("Id","Cliente","Telefono","Razon Social","Whasapp"),show='headings',height=5)
            tree.column("# 1",width=50, anchor=W)
            tree.heading("# 1",text="Codigo")

            tree.column("# 2", width=300, anchor=W)
            tree.heading("# 2",text="Cliente")

            tree.column("# 3", width=275, anchor=W)
            tree.heading("# 3",text="Razon Social")

            tree.column("# 4", width=120, anchor=W)
            tree.heading("# 4",text="Telefono")

            tree.column("# 5", width=120, anchor=W)
            tree.heading("# 5",text="Whasapp")

            
            # Agregar los datos a la tabla
            # Mostrar la tabla

            for row in cclientes.mostrarClientes():
                 tree.insert("","end",values=row)

            #Ejecuatar la función de hacer click y mostrar el resultado en los Entry
            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)



            tree.pack()

            base.mainloop()


        except ValueError as error:
                print("Error al mostrar la interfaz, error: {}".format(error))


def guardarRegistro():
     
     global texBoxId,texBoxCliente,texBoxRazonSocial,texBoxTel,texBoxWhatsapp,texBoxEmail,texBoxDireccion,texBoxDepto,texBoxDistrito,texBoxGiro,texBoxVendedor,texBoxNit,texBoxRegistro,texBoxContacto,comboContribuyente,comboPersona,texBoxObservaciones,groupbox


     try:
          #Verificar si los widgets estan inicializados
          if texBoxCliente is None or texBoxRazonSocial is None or texBoxTel is None or texBoxWhatsapp is None or texBoxEmail is None or texBoxDireccion is None or texBoxDepto is None or texBoxDistrito is None or  texBoxGiro is None or texBoxVendedor is None or texBoxNit is None or texBoxRegistro is None or texBoxContacto is None or texBoxObservaciones is None:
                print("Los Widgets no estan inicializados")
                return
          
          cliente = texBoxCliente.get()
          razon = texBoxRazonSocial.get()
          tel = texBoxTel.get()
          whatsapp = texBoxWhatsapp.get()
          email = texBoxEmail.get()
          direccion = texBoxDireccion.get()
          depto = texBoxDepto.get()
          distrito = texBoxDistrito.get()
          giro = texBoxGiro.get()
          vendedor = texBoxVendedor.get()
          nit = texBoxNit.get()
          registro = texBoxRegistro.get()
          contacto = texBoxContacto.get()
          contribuyente = comboContribuyente.get()
          persona = comboPersona.get()
          observaciones = texBoxObservaciones.get()


          cclientes.ingresarClientes(cliente,razon,tel,whatsapp,email,direccion,depto,distrito,giro,vendedor,nit,registro,contacto,contribuyente,persona,observaciones)
          messagebox.showinfo("INFORMACION","Los datos fueron guardados correctamente!!!")

          actualizarTreeView()




          # Limpiamos los campos

          texBoxCliente.delete(0,END)
          texBoxRazonSocial.delete(0,END)
          texBoxTel.delete(0,END)
          texBoxWhatsapp.delete(0,END)
          texBoxEmail.delete(0,END)
          texBoxDireccion.delete(0,END)
          texBoxDepto.delete(0,END)
          texBoxDistrito.delete(0,END)
          texBoxGiro.delete(0,END)
          texBoxVendedor.delete(0,END)
          texBoxNit.delete(0,END)
          texBoxRegistro.delete(0,END)  
          texBoxContacto.delete(0,END)
          texBoxObservaciones.delete(0,END)

     except ValueError as error:
        print("Error al ingresar los datos {}".format(error))


def actualizarTreeView():
     global tree

     try:
          #Borrar todos los elementos actuales del TreeView
          tree.delete(*tree.get_children())

          #Obtener los nuevos datos que deseamos mostrar
          datos = cclientes.mostrarClientes()

          #Insertar los nuevos datos en el TreeView

          for row in cclientes.mostrarClientes():
            tree.insert("","end",values=row)
     except  ValueError as error:
          print("Error al actualizar tabla{}".format(error))

def seleccionarRegistro(event):
         try:
               
               itemSeleccionado = tree.focus()

               if itemSeleccionado:
                    #Obtener los valores por calumna
                    values = tree.item(itemSeleccionado)['values']

                    #Establecer los valores de los widgests Entry

                    texBoxId.delete(0,END)
                    texBoxId.insert(0,values[0])
                    texBoxCliente.delete(0,END)
                    texBoxCliente.insert(0,values[1])
                    texBoxRazonSocial.delete(0,END)
                    texBoxRazonSocial.insert(0,values[2])
                    texBoxTel.delete(0,END)
                    texBoxTel.insert(0,values[3])
                    texBoxWhatsapp.delete(0,END)
                    texBoxWhatsapp.insert(0,values[4])
                    texBoxEmail.delete(0,END)
                    texBoxEmail.insert(0,values[5])
                    texBoxDireccion.delete(0,END)
                    texBoxDireccion.insert(0,values[6])
                    texBoxDepto.delete(0,END)
                    texBoxDepto.insert(0,values[7])
                    texBoxDistrito.delete(0,END)
                    texBoxDistrito.insert(0,values[8])
                    texBoxGiro.delete(0,END)
                    texBoxGiro.insert(0,values[9])
                    texBoxVendedor.delete(0,END)
                    texBoxVendedor.insert(0,values[10])
                    texBoxNit.delete(0,END)
                    texBoxNit.insert(0,values[11])
                    texBoxRegistro.delete(0,END)
                    texBoxRegistro.insert(0,values[12])
                    texBoxContacto.delete(0,END)
                    texBoxContacto.insert(0,values[13])
                    comboContribuyente.set(values[14])
                    comboPersona.set(values[15])
                    texBoxObservaciones.delete(0,END)
                    texBoxObservaciones.insert(0,values[16])

         except ValueError as error:
               print("Error al seleccionar registro {}".format(error))


def modificarRegistro():
     
     global texBoxId,texBoxCliente,texBoxRazonSocial,texBoxTel,texBoxWhatsapp,texBoxEmail,texBoxDireccion,texBoxDepto,texBoxDistrito,texBoxGiro,texBoxVendedor,texBoxNit,texBoxRegistro,texBoxContacto,comboContribuyente,comboPersona,texBoxObservaciones,groupbox


     try:
          #Verificar si los widgets estan inicializados
          if texBoxId is None or texBoxCliente is None or texBoxRazonSocial is None or texBoxTel is None or texBoxWhatsapp is None or texBoxEmail is None or texBoxDireccion is None or texBoxDepto is None or texBoxDistrito is None or  texBoxGiro is None or texBoxVendedor is None or texBoxNit is None or texBoxRegistro is None or texBoxContacto is None or texBoxObservaciones is None:
                print("Los Widgets no estan inicializados")
                return
          
          id = texBoxId.get()
          cliente = texBoxCliente.get()
          razon = texBoxRazonSocial.get()
          tel = texBoxTel.get()
          whatsapp = texBoxWhatsapp.get()
          email = texBoxEmail.get()
          direccion = texBoxDireccion.get()
          depto = texBoxDepto.get()
          distrito = texBoxDistrito.get()
          giro = texBoxGiro.get()
          vendedor = texBoxVendedor.get()
          nit = texBoxNit.get()
          registro = texBoxRegistro.get()
          contacto = texBoxContacto.get()
          contribuyente = comboContribuyente.get()
          persona = comboPersona.get()
          observaciones = texBoxObservaciones.get()


          cclientes.modificarClientes(id,cliente,razon,tel,whatsapp,email,direccion,depto,distrito,giro,vendedor,nit,registro,contacto,contribuyente,persona,observaciones)
          messagebox.showinfo("INFORMACION","Los datos fueron ELIMINADOS correctamente!!!")

          actualizarTreeView()




          # Limpiamos los campos

          texBoxId.delete(0,END)
          texBoxCliente.delete(0,END)
          texBoxRazonSocial.delete(0,END)
          texBoxTel.delete(0,END)
          texBoxWhatsapp.delete(0,END)
          texBoxEmail.delete(0,END)
          texBoxDireccion.delete(0,END)
          texBoxDepto.delete(0,END)
          texBoxDistrito.delete(0,END)
          texBoxGiro.delete(0,END)
          texBoxVendedor.delete(0,END)
          texBoxNit.delete(0,END)
          texBoxRegistro.delete(0,END)  
          texBoxContacto.delete(0,END)
          texBoxObservaciones.delete(0,END)

     except ValueError as error:
        print("Error al modificar los datos {}".format(error))



def eliminarRegistro():
     
     global texBoxId,texBoxCliente,texBoxRazonSocial,texBoxTel,texBoxWhatsapp,texBoxEmail,texBoxDireccion,texBoxDepto,texBoxDistrito,texBoxGiro,texBoxVendedor,texBoxNit,texBoxRegistro,texBoxContacto,comboContribuyente,comboPersona,texBoxObservaciones,groupbox


     try:
          #Verificar si los widgets estan inicializados
          if texBoxId is None:
                print("Los Widgets no estan inicializados")
                return
          
          id = texBoxId.get()


          cclientes.eliminarClientes(id)
          messagebox.showinfo("INFORMACION","Los datos fueron ELIMINADOS correctamente!!!")

          actualizarTreeView()




          # Limpiamos los campos

          texBoxId.delete(0,END)
          texBoxCliente.delete(0,END)
          texBoxRazonSocial.delete(0,END)
          texBoxTel.delete(0,END)
          texBoxWhatsapp.delete(0,END)
          texBoxEmail.delete(0,END)
          texBoxDireccion.delete(0,END)
          texBoxDepto.delete(0,END)
          texBoxDistrito.delete(0,END)
          texBoxGiro.delete(0,END)
          texBoxVendedor.delete(0,END)
          texBoxNit.delete(0,END)
          texBoxRegistro.delete(0,END)  
          texBoxContacto.delete(0,END)
          texBoxObservaciones.delete(0,END)
          

     except ValueError as error:
        print("Error al eliminar los datos {}".format(error))               




Formulario()