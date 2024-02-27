import os
def crearMenu():
    titulo= """
        ++++++++++++++++++++++++
        +     EMICION DE CO2   +
        ++++++++++++++++++++++++
        """
    print(titulo)
    listMenu=[1,2,3,4,5,]

    try:
        print(" 1.Registrar Dependencia\n 2.Registrar consumo por dependencia\n 3.Ver CO2 producido\n 4.Dependencia que produce mayor CO2\n 5.Salir")
        1. 
        op=int(input('--'))

        if (op not in listMenu):
            os.system('cls')
            crearMenu()

    except:
        os.system('pause')
        crearMenu()
        
    else:
        return op