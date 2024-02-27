import os
from tabulate import tabulate
def registCiudad(ciudad:list):
    nombre=input('Ingrese el nombre de la ciudad: ')
    ciudad.append([nombre,0,0,0,0,0])
    os.system('cls')
    return ciudad
def registroSismos(ciudad:list):

    for i in range(len(ciudad)):
        print(f'{i+1}.{ciudad[i][0]}')
    numer=int(input('Seleccione una ciudad para Registrar un sismo: '))
    

    if 0 in ciudad[numer-1]:
        registro=float(input('Ingrese la magnitud: '))
        pos=ciudad[numer-1].index(0)
        ciudad[numer-1][pos]=registro
    else:
        print("No se Pueden agregar mas registros a esta ciudad.")
    os.system('cls')
    return(ciudad)
    
def buscarSismo(ciudad:list):
    for i in range(len(ciudad)):
        print(f'{i+1}.{ciudad[i][0]}')
    try:
        numer=int(input('Seleccione la ciudad a la que desea ver los sismos registrados: '))
        if 1 <= numer <= len(ciudad):
            ciudad_seleccionada = ciudad[numer - 1]
            print(f'Sismos registrados en la ciudad {ciudad_seleccionada[0]}:')
            
            for i in range(1, len(ciudad_seleccionada)):
                print(f'R{i}. {ciudad_seleccionada[i]}')
            os.system('pause')
        else:
            print('Número de ciudad no válido.')
        
    except ValueError:
        print('Número de ciudad no válido.')
        buscarSismo(ciudad)

    return(ciudad)

def informe(ciudad: list):
    theaders = ['Ciudad', 'R1', 'R2', 'R3', 'R4', 'R5']
    print(tabulate(ciudad, headers=theaders, tablefmt='grid'))
    tipoAlerta=[]
    promedio=0
    
    for i in range(len(ciudad)):
        registros=ciudad[i][1:]
        suma=sum(registros)
        promedio=(suma/5)
        if promedio < 2.5:
            Nivelderiesgo='Amarillo (Sin riesgo)'
        elif 2.6 <= promedio <= 4.5:
            Nivelderiesgo=' Naranja (Riesgo medio)'
        else:
            Nivelderiesgo=' Rojo (Riesgo alto)'
        tipoAlerta.append([ciudad[i][0],promedio,Nivelderiesgo])
    iheaders = ['Ciudad', 'Promedio', 'Tipo de Riesgo']
    print(tabulate(tipoAlerta, headers=iheaders, tablefmt='grid'))
    os.system('pause')
            

    

    


    