from claseUsuario import Usuario
# Se define una nueva clase llamada Administrador que hereda de la clase Usuario. 
class Administrador(Usuario):
    #El constructor se utiliza para inicializar los atributos de un objeto de tipo Administrador.
    #se pasan los argumentos userId, password, loginStatus y registerDate utilizando super() para inicializar los atributos de autenticación heredados de la clase base.
    #adminName y email son atributos privados específicos de la clase Administrador que almacenan el nombre del administrador y su dirección de correo electrónico.
    def __init__(self, userId, password, loginStatus, registerDate, adminName, email):
        super().__init__(userId, password, loginStatus, registerDate)
        self.__adminName = adminName
        self.__email = email

    #
    #El método get acepta un argumento llamado name, que se utiliza para especificar qué atributo se desea obtener de la instancia Administrador.
    #Si name es igual a "userId", "password", "loginStatus" o "registerDate", el método utiliza super().get() para llamar al método get de la clase base Usuario.
    #Si name es igual a "adminName" o "email", el método accede directamente a los atributos privados de la instancia Administrador
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


    #El método set acepta dos argumentos: name y valor. name se utiliza para especificar cuál atributo se desea modificar, y valor es el nuevo valor que se asignará al atributo.
    #Si name es igual a "userId", "password", "loginStatus" o "registerDate", el método utiliza super().set() para llamar al método set de la clase base Usuario.
    #Esto permite modificar los valores de estos atributos heredados de la clase base.
    #Si name es igual a "adminName" o "email", el método asigna directamente el nuevo valor valor a los atributos privados de la instancia Administrador.
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


    #El metodo updateCatalog acepta tres argumentos: adminName, email y password, que representan los valores que se desean verificar en relación con la instancia de Administrador.
    #dentro del método, se utilizan llamadas al método get para obtener los valores actuales de los atributos adminName, email y password de la instancia de Administrador.
    #se realiza una comparación de igualdad para verificar si los valores obtenidos a través del método get coinciden con los valores proporcionados como argumentos.
    def updateCatalog(self, adminName, email, password):
        return True if((self.get("adminName")==adminName)&(self.get("email")==email)&(self.get("password")==password)) else False




