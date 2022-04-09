class Persona:
    def __init__(self):
        self.__noControl=0
        self.__nombre=""
        self.__departamento=0
        self.__sueldohr=0.0
        self.__numhrs=0
        self.__salario=0.0
    # ASIGNA INFORMACION A CADA UNO DE LOS ATRIBUTOS DE LA CLASE
    def ingresarNoControl(self, noControl):
        self.__noControl=noControl

    def ingresarNombre(self, nombre):
        self.__nombre=nombre

    def ingresarDepto(self, departamento):
        self.__departamento=departamento
    def ingresarSueldoHr(self, sueldohr):
        self.__sueldohr=sueldohr
    def ingresarNumHrs(self, numhrs):
        self.__numhrs=numhrs
    def calcularSalario(self):
        self.__salario=self.__sueldohr*self.__numhrs
        return self.__salario
    # RECUPERA CADA UN DE LOS DATOS DE LA CLASE EMPLEADO
    def getControl(self):
        return self.__noControl
    def getNombre(self):
        return self.__nombre
    def getDepto(self):
        return self.__departamento
    def getSueldo(self):
        return self.__sueldohr
    def getNumHrs(self):
        return self.__numhrs

    # SE IMPRIMEN LOS DATOS DE CADA EMPLEADO

    def imprimir(self):
        print("Clave: ", self.getControl())
        print("Nombre: ", self.getNombre())
        print("Departamento: ", self.getDepto())
        print("Sueldo por hora: ", self.getSueldo())
        print("Numero de horas-trabajo: ", self.getNumHrs())
        print("Salario: ", self.calcularSalario())




