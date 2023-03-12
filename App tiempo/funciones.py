def listarCiudades(ciudades):
    
    print("Ciudades: ")
    contador = 1
    for c in ciudades:
        datos = "{0}. Ciudad: {1} | Tiempo: {2} | Celcius: {3}° "
        print(datos.format(contador, c[0], c[1], c[2]))
        contador = contador + 1
    print(" ")
    
def eliminarCiudad(ciudades):
    listarCiudades(ciudades)
    existeC = False
    cEliminar = input("Ingrese la ciudad a eliminar:")
    for c in ciudades:
        if c[0] == cEliminar:
            existeC = True
            break
    if not existeC:
        cEliminar = ""

    return cEliminar

def listarCiudad(ciudad):
    
    datos = "::::: Ciudad: {1} | Tiempo: {2} | Celcius: {3}::::: "
    print(datos.format(ciudad[0], ciudad[1], ciudad[2]))
        
