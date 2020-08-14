class Producto:
    def __init__(self,nombre,precio,precioCuidado=False,primeraNecesidad=False,descuento = 0):
        self.nombre = nombre
        self.precio = precio
        self.precioCuidado = precioCuidado
        self.primeraNecesidad = primeraNecesidad
        if self.primeraNecesidad == True:
            self.descuento = (100-descuento)/100
            self.precio = self.precio*self.descuento
    
    def imprimir(self):
        if (self.precioCuidado == False):
            esCuidado = "No"
        else:
            esCuidado = "Si"
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Precio Cuidado: {esCuidado}, Es de primera necesidad: {self.primeraNecesidad}, Descuento: {self.descuento}")
