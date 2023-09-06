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

  # Método para obtener el valor de una variable de instancia
def get(self, name):
    # Si el nombre es "orderId", devuelve el valor de la variable __orderId
    if(name=="orderId"):
        return self.__orderId
    # Si el nombre es "productId", devuelve el valor de la variable __productId
    elif(name=="productId"):
        return self.__productId
    # Si el nombre es "quantity", devuelve el valor de la variable __quantity
    elif(name=="quantity"):
        return self.__quantity
    # Si el nombre es "unitCost", devuelve el valor de la variable __unitCost
    elif(name=="unitCost"):
        return self.__unitCost
    # Si el nombre es "subtotal", devuelve el valor de la variable __subtotal
    elif(name=="subtotal"):
        return self.__subtotal

# Método para establecer el valor de una variable de instancia
def set(self, name, valor):
    # Si el nombre es "orderId", establece el valor de la variable __orderId
    if(name=="orderId"):
        self.__orderId = valor
    # Si el nombre es "productId", establece el valor de la variable __productId
    elif(name=="productId"):
        self.__productId = valor
    # Si el nombre es "quantity", establece el valor de la variable __quantity y recalcula el subtotal
    elif(name=="quantity"):
        self.__quantity = valor
        self.__subtotal = self.calcPrice()
    # Si el nombre es "unitCost", establece el valor de la variable __unitCost y recalcula el subtotal
    elif(name=="unitCost"):
        self.__unitCost = valor
        self.__subtotal = self.calcPrice()

    
    # Método para calcular el precio del pedido
    def calcPrice(self):
        # Calcula el precio multiplicando la cantidad por el costo unitario
        price = self.__quantity*self.__unitCost
        # Devuelve el precio calculado
        return price



