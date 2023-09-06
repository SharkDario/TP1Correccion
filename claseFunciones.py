from claseComestible import Comestible

from datetime import datetime
#clase estatica, porque todos los metodos son estaticos
class Funciones(): 
    #Este constructor se utiliza para crear objetos de la clase Funciones. 
    #listaTiendas, nombreProducto, y listaProductos son parámetros que se pasan al constructor cuando 
    #se crea un objeto de la clase Funciones. Estos parámetros son valores que se utilizan para inicializar 
    #los atributos del objeto se vuelven privados para evitar que se accedan a estos directamente
    def __init__(self, listaTiendas, nombreProducto, listaProductos):
        self.__listaTiendas = listaTiendas
        self.__nombreProducto = nombreProducto
        self.__listaProductos = listaProductos
    #En este metodo publico get utilizamos una serie de condiciones para determinar cuales de los atributos se debe
    #devolver del valor "name", si name es igual a "listaTiendas", el metodo devuelve el valor del atributo privado __listaTiendas
    #si no devuelve el valor del atributo privado __nombreProducto por ultimo si no coincide con ninguno de los dos devuelve el atributo __listaP
    def get(self, name):
        if(name=="listaTiendas"):
            return self.__listaTiendas
        elif(name=="nombreProducto"):
            return self.__nombreProducto
        else:
            return self.__listaP
    #En este metodo publico set lo ultilizamos para modificar los atributos privados con una serie de condiciones donde
    #Si name es igual a "listaTiendas", el metodo establece el valor del atributo privado __listaTiendas en valor lo mismo
    #en "nombreProducto" , si no coincide con ninguno de los valores anteriores, el metodo establece un atributo __listaP en valor.
    def set(self, name, valor):
        if(name=="listaTiendas"):
            self.__listaTiendas = valor
        elif(name=="nombreProducto"):
            self.__nombreProducto = valor
        else:
            self.__listaP = valor
    #@staticmethod para convertir la funcion a un metodo estatico para poder utilizarlo en el principal
    #este metodo estatico calcula la media de los precios de un producto en una lista de tiendas, sumando los precios de dicho producto en 
    #todas las tiendas y dividiendo la suma entre el numero de tiendas.
    @staticmethod 
    def calcularMedia(listaTiendas, nombreProducto):
        acumulador = 0
        for tienda in listaTiendas:
            listaProductos = tienda.get("listaProductos")
            for producto in listaProductos:
                if(nombreProducto==(producto.get("nombre"))):
                    acumulador += producto.get("precioVenta")
                    break
        nTiendas = len(listaTiendas)
        return (acumulador/nTiendas)
    #@staticmethod para convertir la funcion a un metodo estatico para poder utilizarlo en el principal
    #creamos esta lista de productos para ser utilizados luego en el programa principal
    #se utiliza el modulo datetime para establecer la fecha de caducidad de los productos
    @staticmethod 
    def obtenerListaProductos():
        producto1 = Comestible("harina", 1000, datetime.strptime('5:9:2023', '%d:%m:%Y'))
        producto2 = Comestible("azucar", 1600,datetime.strptime('5:9:2023', '%d:%m:%Y'))
        producto3 = Comestible("leche", 2000, datetime.strptime('5:9:2023', '%d:%m:%Y'))
        listaProductos = [producto1, producto2, producto3]
        return listaProductos
    #@staticmethod para convertir la funcion a un metodo estatico para poder utilizarlo en el principal
    #creamos esta lista de productos para ser utilizados luego en el programa principal
    @staticmethod
    def listaProductosATexto(listaProductos):
        textoProductos = ""
        for producto in listaProductos:
            textoProductos += (producto.mostrarProducto()+"\n")
        return textoProductos





