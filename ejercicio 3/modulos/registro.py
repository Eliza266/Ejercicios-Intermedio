from tabulate import tabulate
import os

def addProductos(productos: dict):
    productoN = {
        'codigo': input('Ingrese el código del producto: '),
        'nombre': input('Ingrese el nombre del producto: '),
        'valorCosto': float(input('Ingrese el valor de costo del producto: ')),
        'valorVenta': float(input('Ingrese el valor de venta del producto: ')),
        'stock': int(input('Ingrese el stock  del producto: ')),
        'stockMax': int(input('Ingrese el stock máximo del producto: ')),
        'stockMin': int(input('Ingrese el stock mínimo del producto: ')),
        'proveedor': input('Ingrese el proveedor del producto: ')
    }
    productos[productoN['codigo']] = productoN
def visualizacion(productos: dict):
   
    data_productos = [[k, *v.values()] for k, v in productos.items()]

    theaders = ['Código', 'Nombre', 'Valor Costo', 'Valor Venta', 'Stock','StockMax', 'Stock Mínimo', 'Proveedor']
    print(tabulate(data_productos, headers=theaders, tablefmt='fancy_grid', showindex=False))
    

    os.system('pause')
    os.system('cls')

def actualStock(productos:dict):
    try:

        codigo=input('Ingrese el codigo del producto')
        if codigo in productos:
            stock=int(input('Ingrese el valor del stock del producto'))
            if stock> productos[codigo]['stockMax']:
                print('Error, Debe ingresar un valor menor al Stok Maximo')
                actualStock(productos)
            else:
                productos[codigo]['stock']=stock
                print(productos[codigo])
                os.system('pause')
        else:
            print('Codigo de Producto no registrado')
            actualStock(productos)
    except ValueError:
        print('Valor Incorrecto')
        actualStock(productos)
    else: 
        return productos
    os.system('pause')
    os.system('cls')
def informe(productos: dict):
    theaders = ['Código','Nombre']
    productosEstadoCritico = [] 
    for key, codigo in productos.items():
        stock = productos[key].get('stock', 0)
        stock_min = productos[key].get('stockMin', 0)
        if stock < stock_min:
            nombre_producto = codigo.get('nombre', 'Nombre no disponible')
            codigo_producto = key
            productosEstadoCritico.append([codigo_producto,nombre_producto])
    print('''
    *******************************
    * PRODUCTOS EN ESTADO CRITICO *
    *******************************
    '''
    )
    print(tabulate(productosEstadoCritico, headers=theaders,tablefmt='heavy_grid'))
    os.system('pause')
    os.system('cls')
        
    
def ganancias(productos:dict):
    ganancia=0
    gananciaTotal=0
    for key, codigo in productos.items():
        costo = productos[key].get('valorCosto', 0)
        vVenta= productos[key].get('valorVenta', 0)
        stock = productos[key].get('stock', 0)
        ganancia=(vVenta-costo)*stock
        gananciaTotal+=ganancia
    print(f'La ganancia Potencial es: {gananciaTotal} $')
    os.system('pause')
    os.system('cls')
    
