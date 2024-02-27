# En el contexto de la gestión de inventarios, se requiere desarrollar un programa en Python que permita
# realizar el control detallado de productos en un negocio. Cada producto estará caracterizado por los siguientes
# atributos:
# •Código del producto.
# •Nombre del producto.
# •Valor de compra del producto.
# •Valor de venta del producto.
# •Stock mínimo permitido.
# •Stock máximo permitido.
# •Nombre del proveedor del producto.
# 1.Registro de Productos:
# 2.Visualización de Productos:
# 3.Actualización de Stock:
# 4. Informe de Productos Críticos:
# 5. Cálculo de Ganancia Potencial:
import modulos.menu as mp
import modulos.registro as re
if __name__ == '__main__':
    # esta lista inicial es para hacer pruebas
    productos={
        '123':{
                'codigo': 123,
                'nombre': 'Aceite',
                'valorCosto':500,
                'valorVenta': 1000 ,
                'stock':1,
                'stockMax':20,
                'stockMin':2,
                'proveedor':'Pedro'
                },
        '456':{
                'codigo': 456,
                'nombre': 'Arroz',
                'valorCosto':1000,
                'valorVenta': 3000 ,
                'stock':2,
                'stockMax':20,
                'stockMin':5,
                'proveedor':'Pedro'
                }

            }
    principal=True
    while principal:
        op=mp.crearMenu()
        if (op==1):
             rProducto=True
             while rProducto:   
                 
                 re.addProductos(productos)
                 rProducto=bool(input('Ingrese S(si) si desea agregar otro Producto o enter(No)'))
                 mp.os.system('clr')
        elif (op==2):
            re.visualizacion(productos)
        elif (op==3):
            re.actualStock(productos)
        elif (op==4):
            re.informe(productos)
        elif (op==5):
            re.ganancias(productos)
        elif (op==6):
            principal=False
