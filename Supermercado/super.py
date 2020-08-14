from Producto import *

class Supermercado:
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
        
    
    def cantProductos(self,listaProductos):
        print(len(listaProductos)) 
        return len(listaProductos)


    def sumTotPreciosProductos(self,listaProductos):
        suma = 0
        for lista in listaProductos:
            suma += lista.precio
        print (suma)
        return suma

class Catalogo:
    pass




producto1 = Producto("Harina",80,False,True,8)
producto2 = Producto("Arroz",90,True,False)

lista = [producto1,producto2]

super = Supermercado("Algún chino","Av. San Martin 900")

super.cantProductos(lista)
super.sumTotPreciosProductos(lista)