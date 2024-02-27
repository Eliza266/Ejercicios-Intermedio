import os
def crearMenu():
    titulo= """
        +++++++++++++++++++++++++++++++++++++++++
        +     REGISTRO DE SISMOS DE COLOMBIA    +
        +++++++++++++++++++++++++++++++++++++++++
        """
    print(titulo)
    listMenu=[1,2,3,4,5]

    try:
        print(" 1.Registrar Ciudad\n 2.Registrar Sismo\n 3.Buscar Sismos Por Ciudad\n 4.Informe \n 5.Salir")
        op=int(input('--'))
        if (op not in listMenu):
            os.system('cls')
            crearMenu()

    except:
        os.system('pause')
        crearMenu()
        
    else:
        return op