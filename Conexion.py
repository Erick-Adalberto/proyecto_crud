# Hemos utilizado el comando "pip install mysql-connector-python" desde la terminal de VisualCode para descargar e instalar la libreria necesaria para hacer la coneccion de la base de datos a mi programa

import mysql.connector

class CConexion:
  def ConexionBaseDeDatos():
    try:
           conexion = mysql.connector.connect(user='root',password='tecnologica',
                                              host='127.0.0.1',
                                              database='facturacion',
                                              port='3306')

           print("Conexion Establecida Correctamente")

           return conexion

    except mysql.connector.Error as error:
        print("Error al conectarse a la Base de Datos {}".format(error))    
        return conexion
        

  ConexionBaseDeDatos()