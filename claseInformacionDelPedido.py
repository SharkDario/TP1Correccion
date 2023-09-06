
class InformacionDelPedido(object):
    def __init__(self, shippingId, shippingType, shippingCost, shippingRegionId):
        self.__shippingId = shippingId
        self.__shippingType = shippingType
        self.__shippingCost = shippingCost
        self.__shippingRegionId = shippingRegionId

    def updateShippingInfo(self, shippingId, shippingType, shippingCost, shippingRegionId):
        self.__shippingId = shippingId
        self.__shippingType = shippingType
        self.__shippingCost = shippingCost
        self.__shippingRegionId = shippingRegionId


