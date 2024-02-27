import os
def crearMenu():
    titulo= """
        +++++++++++++++++++++++++++++++++++++++++
        +     INVENTARIO DE PRODUCTOS           +
        +++++++++++++++++++++++++++++++++++++++++
        """
    print(titulo)
    listMenu=[1,2,3,4,5,6]

    try:
        print(" 1.Registro de productos\n 2.Visualizacion de Productos\n 3.Actualizacion de Stock\n 4.Informe de productos Criticos\n 5.Calculo de ganancia potencial\n 6.Salir")
        op=int(input('--'))
        if (op not in listMenu):
            os.system('cls')
            crearMenu()

    except:
        os.system('pause')
        crearMenu()
        
    else:
        return op