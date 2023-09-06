from claseUsuario import Usuario

class Cliente(Usuario):
    def __init__(self, userId, password, loginStatus, registerDate, customerName, address, email, creditCardInfo, accountBalance, shippingInfo=[]):
        super().__init__(userId, password, loginStatus, registerDate)
        self.__customerName = customerName
        self.__address = address
        self.__email = email
        self.__creditCardInfo = creditCardInfo
        #lista de carritos y pedidos, porque un cliente puede tener muchos carritos y muchos pedidos
        self.__shippingInfo = shippingInfo 
        self.__accountBalance = accountBalance

    def get(self, name):
        if(name=="userId"):
            return super().get("userId")
        elif(name=="password"):
            return super().get("password")
        elif(name=="loginStatus"):
            return super().get("loginStatus")
        elif(name=="registerDate"):
            return super().get("registerDate")
        elif(name=="customerName"):
            return self.__customerName
        elif(name=="address"):
            return self.__address
        elif(name=="email"):
            return self.__email
        elif(name=="creditCardInfo"):
            return self.__creditCardInfo
        elif(name=="shippingInfo"):
            return self.__shippingInfo
        elif(name=="accountBalance"):
            return self.__accountBalance

    def set(self, name, valor):
        if(name=="userId"):
            super().set("userId", valor)
        elif(name=="password"):
            super().set("password", valor)
        elif(name=="loginStatus"):
            super().set("loginStatus", valor)
        elif(name=="registerDate"):
            super().set("registerDate", valor)
        elif(name=="customerName"):
            self.__customerName = valor
        elif(name=="address"):
            self.__address = valor
        elif(name=="email"):
            self.__email = valor
        elif(name=="creditCardInfo"):
            self.__creditCardInfo = valor
        elif(name=="shippingInfo"):
            self.__shippingInfo = valor
        elif(name=="accountBalance"):
            self.__accountBalance = valor

    def register(self, email, password):
        self.__email = email
        self.__password = password

    def login(self, email, password):
        return True if((self.__email==email)&(self.__password==password)) else False

    def updateProfile(self, password, customerName, address, email, creditCardInfo):
        self.set("password", password)
        self.set("customerName", customerName)
        self.set("address", address)
        self.set("email", email)
        self.set("creditCardInfo", creditCardInfo)

    def agregarPedidoCarrito(self, pedidoOCarrito):
        self.__shippingInfo.append(pedidoOCarrito)


