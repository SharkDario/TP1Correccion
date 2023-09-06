from datetime import datetime

class CarritoDeCompras():
    def __init__(self, cardId):
        self.__cardId = cardId
        self.__productID = {}

    def __diccionarioProductosATexto(self):
        texto=""
        for clave, valor in self.__productID:
            texto+=f'ID producto: {clave} - Cantidad: {valor[0]} - Fecha: {valor[1]} - Precio: {valor[2]}\n'
        return texto

    def __cuentaTotal(self):
        cuenta = 0
        for clave, valor in self.__productID:
            cuenta+= valor[2]
        return cuenta

    def addCartItem(self, productID, quantity, dateAdded, price):
        price = price * quantity
        self.__productID[productID] = [quantity, datetime.strftime(dateAdded, '%d/%m/%Y'), price]

    def updateQuantity(self, productID, quantity, dateAdded):
        if productID in self.__productID:
            price = price * quantity
            self.__productID[productID] = [quantity, datetime.strftime(dateAdded, '%d/%m/%Y'), price]

    def viewCartDetails(self):
        return f'ID del carrito de compras: {self.__cardId}\nLista de productos:\n{self.__diccionarioProductosATexto()}'

    def checkOut(self):
        return f'Cuenta total: ${self.__cuentaTotal}'
        


