#Llmao a la libreria abc
from abc import ABC, abstractmethod

class Aeropuerto(ABC):
    def __init__(self):
        self.codigo = int
        self.direccion = str
        self.telefono = int
        self.plazas = int
        self.nombre = str
        self.numVuelo = int
        self.fecha = str
        self.hora = str
        self.origen = str
        self.destino = str
        self.plazaTurista = int

    @abstractmethod
    def __str__(self):
        pass

class Añadir(ABC):
    @abstractmethod
    def agregarDatos(self):
        pass

    @abstractmethod
    def registroDatos(self):
        pass

class Menus(ABC):
    @abstractmethod
    def mainClass(self):
        pass

    @abstractmethod
    def agregarDatos(self):
        pass

    @abstractmethod
    def printDatos(self):
        pass

    