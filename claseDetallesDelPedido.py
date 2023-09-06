class DetallesDelPedido():
    # Constructor de la clase DetallesDelPedido
    def __init__(self, orderId, productId, productName, quantity, unitCost):
        # Inicializa las variables de instancia con los valores de los parámetros
        self.__orderId = orderId
        self.__productId = productId
        self.__productName = productName
        self.__quantity = quantity
        self.__unitCost = unitCost
        # Calcula el subtotal del pedido llamando al método calcPrice()
        self.__subtotal = self.calcPrice()

    # Método para calcular el precio del pedido
    def calcPrice(self):
        # Calcula el precio multiplicando la cantidad por el costo unitario
        price = self.__quantity*self.__unitCost
        # Devuelve el precio calculado
        return price



