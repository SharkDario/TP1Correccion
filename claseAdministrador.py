from claseUsuario import Usuario

class Administrador(Usuario):
    def __init__(self, userId, password, loginStatus, registerDate, adminName, email):
        super().__init__(userId, password, loginStatus, registerDate)
        self.__adminName = adminName
        self.__email = email

    def get(self, name):
        if(name=="userId"):
            return super().get("userId")
        elif(name=="password"):
            return super().get("password")
        elif(name=="loginStatus"):
            return super().get("loginStatus")
        elif(name=="registerDate"):
            return super().get("registerDate")
        elif(name=="adminName"):
            return self.__adminName
        elif(name=="email"):
            return self.__email

    def set(self, name, valor):
        if(name=="userId"):
            super().set("userId", valor)
        elif(name=="password"):
            super().set("password", valor)
        elif(name=="loginStatus"):
            super().set("loginStatus", valor)
        elif(name=="registerDate"):
            super().set("registerDate", valor)
        elif(name=="adminName"):
            self.__adminName = valor
        elif(name=="email"):
            self.__email = valor

    def updateCatalog(self, adminName, email, password):
        return True if((self.get("adminName")==adminName)&(self.get("email")==email)&(self.get("password")==password)) else False




