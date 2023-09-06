from datetime import datetime
#Clase abstracta usuario que sera plantilla para clase Cliente y clase Administrador
#La clase Usuario define los atributos y metodos basicos que podrían ser comunes a usuarios en un sistema, como clientes y 
#administradores, esta clase es abstracta y no se pretende que se instancie directamente, sino que se utilice como base para 
#crear clases concretas, como Cliente y Administrador, que heredaran estos atributos y metodos y 
#podran agregar funcionalidades adicionales según sea necesario.
class Usuario():
    def __init__(self, userId, password, loginStatus, registerDate):
        self.__userId = userId
        self.__password = password
        self.__loginStatus = loginStatus
        self.__registerDate = datetime.strftime(registerDate, '%d/%m/%Y')
#la clase Usuario. Recibe cuatro parametros: userId, password, loginStatus, y registerDate.
#Estos parametros se utilizan para inicializar atributos de instancia privados que almacenan la informacion del usuario.
#La fecha proporcionada en registerDate se convierte en una cadena con el formato utilizando el metodo strftime del modulo datetime.
    def get(self, name):
        if(name=="userId"):
            return self.__userId
        elif(name=="password"):
            return self.__password
        elif(name=="loginStatus"):
            return self.__loginStatus
        elif(name=="registerDate"):
            return self.__registerDate
#El metodo get recibe el nombre del atributo que se desea obtener y devuelve su valor correspondiente.
    def set(self, name, valor):
        if(name=="userId"):
            self.__userId = valor
        elif(name=="password"):
            self.__password = valor
        elif(name=="loginStatus"):
            self.__loginStatus = valor
        elif(name=="registerDate"):
            self.__registerDate = valor
#El metodo set recibe el nombre del atributo y el valor al que se desea establecer.
    def verifyLogin(self, user, contra):
        return True if ((self.__userId==user)&(self.__password==contra)) else False
#Este metodo recibe un nombre de usuario (user) y una contraseña (contra) como argumentos y verifica si coinciden con los valores
#almacenados en los atributos __userId y __password, devuelve True si la verificacion es exitosa y False en caso contrario.


