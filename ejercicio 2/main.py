import modulos.menu as mp
import modulos.registro as re
if __name__ == '__main__':
    # esta lista inicial es para hacer pruebas
    dependencias={}
    dependencia={}
    lista=[]
    
    principal=True
    while principal:
        op=mp.crearMenu()
        if (op==1):
              rdependencia=True
              while rdependencia:
                re.registrarDep(dependencias)
                rdependencia=bool(input('Ingrese S(si) si desea agregar otra Dependencia o enter(No)'))
            
        elif (op==2):
            re.registrarConsumo(dependencias,lista)
        elif (op==3):
            re.verCO2(lista)
        elif (op==4):
            re.mayorEmisorCO2(lista)
        elif (op==5):
            principal=False
          





    

    


