from datetime import datetime

class CarritoDeCompras():
    # Constructor de la clase CarritoDeCompras
    def __init__(self, cardId):
        # Inicializa el ID del carrito y el diccionario de productos
        self.__cardId = cardId
        self.__productID = {}

    # Método para obtener el valor de una variable de instancia
def get(self, name):
    # Si el nombre es "cardId", devuelve el valor de la variable __cardId
    if(name=="cardId"):
        return self.__cardId
    # Si el nombre es "productID", devuelve el valor de la variable __productID
    elif(name=="productID"):
        return self.__productID

# Método para establecer el valor de una variable de instancia
def set(self, name, valor):
    # Si el nombre es "cardId", establece el valor de la variable __cardId
    if(name=="cardId"):
        self.__cardId = valor

    
    # Método privado para convertir el diccionario de productos en una cadena de texto legible
    def __diccionarioProductosATexto(self):
        texto=""
        # Itera sobre cada producto en el diccionario
        for clave, valor in self.__productID:
            # Agrega información sobre el producto a la cadena de texto
            texto+=f'ID producto: {clave} - Cantidad: {valor[0]} - Fecha: {valor[1]} - Precio: {valor[2]}\n'
        return texto

    # Método privado para calcular el total del carrito
    def __cuentaTotal(self):
        cuenta = 0
        # Itera sobre cada producto en el diccionario
        for clave, valor in self.__productID:
            # Suma el precio del producto al total del carrito
            cuenta+= valor[2]
        return cuenta

    # Método para agregar un elemento al carrito
    def addCartItem(self, productID, quantity, dateAdded, price):
        # Calcula el precio total del producto
        price = price * quantity
        # Agrega la información del producto al diccionario
        self.__productID[productID] = [quantity, datetime.strftime(dateAdded, '%d/%m/%Y'), price]

    # Método para actualizar la cantidad de un producto en el carrito
    def updateQuantity(self, productID, quantity, dateAdded):
        # Verifica si el producto está en el diccionario
        if productID in self.__productID:
            # Calcula el nuevo precio total del producto
            price = price * quantity
            # Actualiza la información del producto en el diccionario
            self.__productID[productID] = [quantity, datetime.strftime(dateAdded, '%d/%m/%Y'), price]

    # Método para ver los detalles del carrito
    def viewCartDetails(self):
        # Devuelve una cadena de texto con información sobre el carrito y sus productos
        return f'ID del carrito de compras: {self.__cardId}\nLista de productos:\n{self.__diccionarioProductosATexto()}'

    # Método para realizar el pago del carrito
    def checkOut(self):
        # Devuelve una cadena de texto con el total del carrito
        return f'Cuenta total: ${self.__cuentaTotal}'

        


