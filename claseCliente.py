from claseUsuario import Usuario
#define una clase llamada Cliente que hereda de la clase Usuario. 
class Cliente(Usuario):
#El constructor de la clase Cliente se utiliza para inicializar los atributos de un objeto de tipo Cliente.
# se pasan los argumentos userId, password, loginStatus y registerDate utilizando super() para inicializar los atributos de autenticación heredados de la clase base.
#se inicializan varios atributos específicos de la clase Cliente, como customerName, address, email, creditCardInfo, shippingInfo y accountBalance.
    def __init__(self, userId, password, loginStatus, registerDate, customerName, address, email, creditCardInfo, accountBalance, shippingInfo=[]):
        super().__init__(userId, password, loginStatus, registerDate)
        self.__customerName = customerName
        self.__address = address
        self.__email = email
        self.__creditCardInfo = creditCardInfo
        #lista de carritos y pedidos, porque un cliente puede tener muchos carritos y muchos pedidos
        self.__shippingInfo = shippingInfo 
        self.__accountBalance = accountBalance


    #el metodo get permite obtener valores de atributos tanto heredados de la clase base Usuario como específicos de la clase Cliente.
    #Se utilizan super() para acceder al metodo get de la clase base cuando se trata de atributos heredados.
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
            
#El metodo set permite modificar atributos de la instancia
#Se utilizan super() para acceder al metodo set de la clase base cuando se trata de atributos heredados.
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

#El método register acepta dos argumentos: email y password. Estos argumentos representan la dirección de correo electrónico y la contraseña que el cliente desea asociar con su cuenta.
#Dentro del método, se asigna el valor de email al atributo privado __email de la instancia actual de Cliente. Esto actualiza la dirección de correo electrónico del cliente en la instancia.
#se asigna el valor de password al atributo privado password de la instancia actual de Cliente. Esto actualiza la contraseña del cliente en la instancia.
    
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


