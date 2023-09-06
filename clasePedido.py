from claseInformacionDelPedido import InformacionDelPedido
from claseDetallesDelPedido import DetallesDelPedido
from datetime import datetime

class Pedido():
    #El constructor __init__ se utiliza para inicializar un objeto de la clase Pedido cuando se crea una instancia de ella.
    #Dentro del constructor, se formatea la fecha de creación (dateCreated) y la fecha de envío (dateShipped) utilizando el módulo datetime para asegurarse de que estén en el formato 'dd/mm/yyyy'.
    #se crea una instancia de las clases InformacionDelPedido y DetallesDelPedido utilizando ciertos atributos del pedido para almacenar información relacionada con el envío y los detalles del pedido.
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

#Este metodo se utiliza para realizar un pedido en el sistema.
#Toma varios argumentos relacionados con el pedido, como el nombre del cliente, el ID del cliente, el ID del producto, el nombre del producto, la cantidad, el costo unitario, el tipo de envío, el costo de envío y la región de envío.
#Dentro del método, se actualiza la información del pedido (informacionDelPedido) y los detalles del pedido (detallesDelPedido) con la nueva información proporcionada.
    def placeOrder(self, customerName, customerId, productId, productName, quantity, unitCost, shippingType, shippingCost, shippingRegionId):
        self.__informacionDelPedido = InformacionDelPedido(self.__shippingId, shippingType, shippingCost, shippingRegionId)
        self.__detallesDelPedido = DetallesDelPedido(self.__orderId, productId, productName, quantity, unitCost)




