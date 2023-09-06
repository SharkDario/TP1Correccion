#La clase llamada InformacionDelPedido esta diseñada para representar informacion relacionada con el envio de un pedido.
class InformacionDelPedido(object):
    def __init__(self, shippingId, shippingType, shippingCost, shippingRegionId):
        self.__shippingId = shippingId
        self.__shippingType = shippingType
        self.__shippingCost = shippingCost
        self.__shippingRegionId = shippingRegionId
#La clase InformacionDelPedido se utiliza para almacenar informacion sobre como se entregara un pedido, el metodo
#el costo, el ID , y la región del envio. "InformacionDelPedido" recibe cuatro parametros: shippingId, shippingType, 
#shippingCost, y shippingRegionId. Estos parametros se utilizan para inicializar los atributos de instancia privados que almacenan la 
#informacion del envío.
    def updateShippingInfo(self, shippingId, shippingType, shippingCost, shippingRegionId):
        self.__shippingId = shippingId
        self.__shippingType = shippingType
        self.__shippingCost = shippingCost
        self.__shippingRegionId = shippingRegionId
#Este metodo se utiliza para actualizar la informacion de envio. 
#Recibe los mismos parametros que el constructor (shippingId, shippingType, shippingCost, shippingRegionId) y actualiza los atributos de
#instancia correspondientes con los nuevos valores proporcionados.

