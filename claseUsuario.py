from datetime import datetime
#Clase abstracta usuario que sera plantilla
#para clase Cliente y clase Administrador
class Usuario():
    def __init__(self, userId, password, loginStatus, registerDate):
        self.__userId = userId
        self.__password = password
        self.__loginStatus = loginStatus
        self.__registerDate = datetime.strftime(registerDate, '%d/%m/%Y')

    def get(self, name):
        if(name=="userId"):
            return self.__userId
        elif(name=="password"):
            return self.__password
        elif(name=="loginStatus"):
            return self.__loginStatus
        elif(name=="registerDate"):
            return self.__registerDate

    def set(self, name, valor):
        if(name=="userId"):
            self.__userId = valor
        elif(name=="password"):
            self.__password = valor
        elif(name=="loginStatus"):
            self.__loginStatus = valor
        elif(name=="registerDate"):
            self.__registerDate = valor

    def verifyLogin(self, user, contra):
        return True if ((self.__userId==user)&(self.__password==contra)) else False


