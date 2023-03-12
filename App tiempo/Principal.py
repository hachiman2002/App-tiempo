import comrpobar_con
import time
#Comprobando si hay conexion a internet
while True:
    print("Comprobando conexion, espere...")
    time.sleep(2)
    if comrpobar_con.respuesta_conexion is True:
        print("Hay conexion a internet")
        time.sleep(2)
        print("La aplicacion esta lista para ser usada")
        break
    elif comrpobar_con.respuesta_conexion is False:
        print("No hay conexion a internet")  
        time.sleep(2)  
        print("Reintentando conexion")
        time.sleep(2)
        
from DB.conexion import DAO 
import funciones

#Funcion requests
def respuesta():
    import requests

    while True:
        api_key = '30d4741c779ba94c470ca1f63045390a'
        ciudad = input("Enter city: ")
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=imperial&APPID={api_key}")
        if weather_data.json()['cod'] == '404':
            print("Ciudad no encontrada")
        else:
            tiempo = weather_data.json()['weather'][0]['main']
            gradosf = round(weather_data.json()['main']['temp'])
            gradosc = (gradosf-32)/1.8
            lista = [ciudad,tiempo,gradosc]
            return lista 
            
            
#Menu principal
def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("""
            ============ MENU PRINCIPAL============
            1.- Registrar ciudad
            2.- Listar ciudades
            3.- Eliminar ciudad
            4.- Actualizar ciudad
            5.- Salir
            =======================================
            """)
            opcion = int(input("Seleccione una opcion:"))

            if opcion <1 or opcion >5:
                print("Opcion incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar=False
                print("Salio del programa")
                print("!Gracias por usar este sistema¡")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcionPrincipal(opcion)


#Ejecutando las opciones del menu principal
def ejecutarOpcionPrincipal(opcion):
    dao = DAO()
    if opcion == 1:
        ciudad = respuesta()
        dao.registrarCiudad(ciudad)
    elif opcion == 2:
        try:
            ciudades = dao.listarCiudades()
            if len(ciudades)>0:
                funciones.listarCiudades(ciudades)
            else:
                print("No se encontraron ciudades...")
        except:
            print("Ocurrio un error")
    elif opcion == 3:
        try:
            ciudades = dao.listarCiudades()
            if len(ciudades)>0:
                cEliminar = funciones.eliminarCiudad(ciudades)
                if not(cEliminar == ""):
                    dao.eliminarCiudad(cEliminar)
                else: 
                    print("Ciudad no encontrada...\n")
            else:
                            print("No se encontraron ciudades...")
        except:
            print("Ocurrio un error")
    elif opcion == 4:
            try:    
                ciudades = dao.listarCiudades()
                if len(ciudades)>0:
                    ciudad = respuesta()
                    
                    dao.actualizarCiudad(ciudad)
                    
                else:
                    print("No se encontraron ciudades...")
            except:
                print("Ocurrio un error...")
    
    else:
        print("Opcion incorrecta intente denuevo")

menuPrincipal()