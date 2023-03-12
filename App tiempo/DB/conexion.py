import mysql.connector
from mysql.connector import Error
#DATA ACCESS OBJECT

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                    host = 'localhost',
                    user = 'graciany',
                    password = 'Informatica2022',
                    database = 'prueba'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))

    def listarCiudades(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM tiempo ")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
    
    def registrarCiudad(self,ciudad):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("INSERT INTO tiempo (ciudad,tiempo,grados) VALUES ('{0}','{1}',{2})")
                cursor.execute(sql.format(ciudad[0],ciudad[1],ciudad[2]))
                self.conexion.commit()
                print("ciudad registrada")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
    
    def actualizarCiudad(self,ciudad):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE tiempo SET  tiempo='{0}', grados={1} WHERE ciudad='{2}' "
                cursor.execute(sql.format(ciudad[1],ciudad[2],ciudad[0]))
                self.conexion.commit()
                print("¡Ciudad actualizada!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
    
    def eliminarCiudad(self,cEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM tiempo where ciudad = '{0}'"
                cursor.execute(sql.format(cEliminar))
                self.conexion.commit()
                print("¡Ciudad eliminada!")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    def listarCiudad(self,c):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("SELECT * FROM tiempo where ciudad = '{0}'")
                cursor.execute(sql.format(c))
                resultados = cursor.fetchall() 
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
