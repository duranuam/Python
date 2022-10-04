from datetime import datetime
from re import I
""" Clase persona contiene información de una persona.
tales como, su nombre, apellidos, fecha de nacimiento
"""
class Persona:
    def __init__(self, nom, ape, nac):
        self.Nombre = nom
        self.Apellido = ape
        self.AñoNac = nac
    
    def __str__(self):
        return f"""Datos de la Persona
Nombre: {self.Nombre}
Apellido: {self.Apellido}
Fecha de Nac: {self.AñoNac} 
Edad: {self.calcEdad()}"""

    """Calcular la edad de la persona"""
    def calcEdad(self):
        añoAct = datetime.now().year
       
        return añoAct - self.AñoNac

class ListaPersona:
    def __init__(self):
        self.lista = []
    
    """Agrega un nuevo elemento a la lista"""
    def agregar(self, nom, ape, nac):
        pers = Persona(nom, ape, nac)
        self.lista.append(pers)
    

    """Eliminar elemento de la lista"""
    def eliminar(self, pos):
        self.lista.pop(pos)

    """buscar persona por nombre y apellido"""
    def buscar(self, nom, ape):
        posicion = 0
        for pers in self.lista:
            if pers.Nombre == nom and pers.Apellido == ape:
                return posicion
            posicion += 1
    
    def buscarPersona(self, nom, ape):
        for pers in self.lista:
            if pers.Nombre == nom and pers.Apellido == ape:
                print(pers)
            
    

