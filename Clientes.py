from Conexion import *

class cclientes:

    def mostrarClientes():
        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         cursor.execute("SELECT * FROM clientes;")
         miResultado = cursor.fetchall()
         cone.commit()
         cone.close()
         return miResultado
        except mysql.connector.Error as error:
            print("Error al mostrar datos {}".format(error))
       

    def ingresarClientes(Cliente,Razon,Telefono,Whatsapp,Email,Direccion,Departamento,Distrito,Giro,Vendedor,NIT,Registro,Contacto,Contribuyente,Persona,Observaciones):

        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="insert into clientes values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
         #La variable valores tiene que ser una tupla
         #Como minima expresion es: (valor,) la coma hace que sea una tupla
         #Las tuplas son listas inmutables, eso quiere decir que no se pueden modificar.
         valores=(Cliente,Razon,Telefono, Whatsapp,Email,Direccion,Departamento,Distrito,Giro,Vendedor,NIT,Registro,Contacto,Contribuyente,Persona,Observaciones)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Ingresado")


        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))


    def modificarClientes(id,Cliente,Razon,Telefono,Whatsapp,Email,Direccion,Departamento,Distrito,Giro,Vendedor,NIT,Registro,Contacto,Contribuyente,Persona,Observaciones):

        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="UPDATE clientes SET clientes.Cliente = %s,clientes.Razon = %s,clientes.Telefono = %s,clientes.Whatsapp = %s,clientes.Email = %s,clientes.Direccion = %s,clientes.Departamento = %s,clientes.Distrito = %s,clientes.Giro = %s,clientes.Vendedor = %s,clientes.NIT = %s,clientes.Registro = %s,clientes.Contacto = %s,clientes.Contribuyente = %s,clientes.Persona = %s,clientes.Observaciones = %s WHERE clientes.id = %s;"
        
         valores=(Cliente,Razon,Telefono, Whatsapp,Email,Direccion,Departamento,Distrito,Giro,Vendedor,NIT,Registro,Contacto,Contribuyente,Persona,Observaciones,id)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Actualizado")
         cone.close()


        except mysql.connector.Error as error:
            print("Error de actualización de datos {}".format(error))       



    def eliminarClientes(id):

        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="DELETE FROM clientes WHERE id = %s;"
        
         valores=(id,)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro Eliminado")
         cone.close()


        except mysql.connector.Error as error:
            print("Error de eliminación de datos {}".format(error))       