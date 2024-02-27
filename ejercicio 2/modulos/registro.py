from tabulate import tabulate
import os
def registrarDep(dependencias:dict):
    nombre = input(f"Ingrese el nombre de la dependencia: {len(dependencias) + 1}\n")
    dependencia={
        'nombre':nombre,
        'dispositivos':{},
        'eCO2':0
    }
    dependencias[nombre] = dependencia 
    print(dependencia)


def registrarConsumo(dependencias: dict,lista:list):
    print("Nombres de las dependencias registradas:")
    for nombre in dependencias:
        print(nombre)
    emisionTotalDependencia=0
    nombreDepen = input('Ingrese el nombre de la Dependencia a la que desea registrar consumo: ') 
    equi=True
    while equi:

        if nombreDepen in dependencias:
            nombre_dispositivo = input('Ingrese el nombre del dispositivo: ')
            cantidad = int(input(f'Ingrese la cantidad de {nombre_dispositivo}: '))
            potencia = float(input('Ingrese la potencia del Dispositivo: '))
            horas_uso = float(input('Ingrese las horas diarias de uso del dispositivo: '))
            
            consumo_mensual = (((potencia * horas_uso) / 1000) * 30) * cantidad
            eCO2=consumo_mensual*0.374
            dispositivo = {
                'nombre': nombre_dispositivo,
                'consumo': consumo_mensual,
                'eCO2': eCO2
            }

        dependencias[nombreDepen]['dispositivos'][nombre_dispositivo]=dispositivo
        emisionTotalDependencia+=eCO2
        equi=bool(input('Desea agregar otro equipo? s(si) enter(no)'))
    os.system('cls')
    lista.append([nombreDepen,emisionTotalDependencia])
    print(lista)

def verCO2(lista:list):
    print('''   **********EMISION DE CO2 POR DEPENDENCIA***********
''')
    theaders = ['DEPENDENCIA','EMISION DE CO2']
    print(tabulate(lista, headers=theaders, tablefmt='heavy_gird'))
    os.system('pause')

def mayorEmisorCO2(lista):
    mayor=0
    nombre=''
    for i in range(len(lista)):
        if lista[i][1]>mayor:
            mayor=lista[i][1]
            nombre=lista[i][0]
    print(f'La dependencia {nombre} es la mayor emisiora de CO2, con ubna cantidad de: {mayor}')
    os.system('pause')







    

