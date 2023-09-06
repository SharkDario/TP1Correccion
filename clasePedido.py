from claseInformacionDelPedido import InformacionDelPedido
from claseDetallesDelPedido import DetallesDelPedido
from datetime import datetime

class Pedido():
    def __init__(self, orderId, dateCreated, dateShipped, customerName, customerId, status, shippingId, shippingType, shippingCost, shippingRegionId, productId, productName, quantity, unitCost):
        self.__orderId = orderId
        self.__dateCreated = datetime.strftime(dateCreated, '%d/%m/%Y')
        self.__dateShipped = datetime.strftime(dateShipped, '%d/%m/%Y')
        self.__customerName = customerName
        self.__customerId = customerId
        self.__status = status
        self.__shippingId = shippingId
        self.__orderId = orderId
        self.__informacionDelPedido = InformacionDelPedido(shippingId, shippingType, shippingCost, shippingRegionId)
        self.__detallesDelPedido = DetallesDelPedido(orderId, productId, productName, quantity, unitCost)

    def placeOrder(self, customerName, customerId, productId, productName, quantity, unitCost, shippingType, shippingCost, shippingRegionId):
        self.__informacionDelPedido = InformacionDelPedido(self.__shippingId, shippingType, shippingCost, shippingRegionId)
        self.__detallesDelPedido = DetallesDelPedido(self.__orderId, productId, productName, quantity, unitCost)




