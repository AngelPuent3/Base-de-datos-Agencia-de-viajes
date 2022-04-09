class Departamento:
    # DECLARACION DE LOS ATRIBUTOS DE LA CLASE

    def __init__(self):
        __claveDepto=0
        __nombre=""
        __jefe=""
        __telefono=0

    # DECLARACIÓN DE LOS MÉTODOS DE LA CLASE
    def ingresarClave(self,clave):
        self.__claveDepto=clave

    def ingresarNombreDepto(self,nombreDepto):
        self.__nombre=nombreDepto

    def ingresarJefe(self,jefe):
        self.__jefe=jefe

    def ingresarTelefono(self,telefono):
        self.__telefono=telefono

    def imprimirD(self):
        print("No.Departamento: ", self.__claveDepto)
        print("Nombre Departamento: ", self.__nombre)
        print("Jefe: ", self.__jefe)
        print("Telefono: ", self.__telefono)