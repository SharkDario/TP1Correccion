class DetallesDelPedido():
    def __init__(self, orderId, productId, productName, quantity, unitCost):
        self.__orderId = orderId
        self.__productId = productId
        self.__productName = productName
        self.__quantity = quantity
        self.__unitCost = unitCost
        self.__subtotal = self.calcPrice()

    def calcPrice(self):
        price = self.__quantity*self.__unitCost
        return price



