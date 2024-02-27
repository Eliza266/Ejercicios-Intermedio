# 1. El centro de prevención de sismos en Colombia desea realizar un programa que le permita llevar el
# Registro del los sismos presentados en 5 ciudades del país. Por cada ciudad se realizan n cantidad de
# Registros. El programa debe permitir registrar las muestras del movimiento en cada ciudad.
# Requerimientos:
# 1. El programa debe tener un menú con las siguientes opciones
# 1. Registrar Ciudad
# 2. Registrar Sismo
# 3. Buscar sismos por ciudad
# 4. Informe de riesgo
# 5. Salir

# Restricciones:
# 1. Todas las ciudades deben tener la misma cantidad de sismos registrado
# 2. El informe de riesgos presenta la siguiente clasificación:
# 1. Amarillo (Sin riesgo) : El promedio de los sismos es < 2,5
# 2. Naranja (Riesgo medio) : El promedio de los sismos esta entre 2.6 y 4.5
# 3. Rojo (Riesgo alto) : El promedio de los sismos es mayor a 4.5
import modulos.menu as mp
import modulos.registr as re
#import modulos.reportes as r
if __name__ == '__main__':
    ciudad=[]
    principal=True
    while principal:
        op=mp.crearMenu()
        if (op==1):
            rCiudad=True
            while rCiudad:   
                 re.registCiudad(ciudad)
                 rCiudad=bool(input('Ingrese S(si) si desea agregar otra Ciudad o enter(No)'))
                
        elif (op==2):
            rSismo=True
            while rSismo:   
                 re.registroSismos(ciudad)
                 rSismo=bool(input('Ingrese S(si) si desea agregar otro registro de Sismo o enter(No)'))
        
        elif (op==3):
            busSismo=True
            while busSismo:   
                 re.buscarSismo(ciudad)
                 busSismo=bool(input('Ingrese S(si) si desea Buscar otro registro de Sismo o enter(No)'))
            
        elif (op==4):
            re.informe(ciudad)
        elif (op==5):
            principal=False
