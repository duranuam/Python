import Clases as c
import os

lista = c.ListaPersona()

def agregar():
    os.system("cls")
    nom = input("Nombre: ")
    ape = input("Apellidos: ")
    añoNac = int(input("Año de nacimiento: "))
    lista.agregar(nom, ape, añoNac)
    os.system("pause")

def buscarRegistro():
    os.system("cls")
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    lista.buscarPersona(nom, ape)
    os.system("pause")

def eliminarRegistro():
    os.system("cls")
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    pos = lista.buscar(nom, ape)
    lista.eliminar(pos)
    os.system("pause")

def mostrarRegistros():
    os.system("cls")
    for reg in lista.lista:
        print(reg)
    os.system("pause")

def menu():
    os.system("cls")
    print("1. Agregar Registros")
    print("2. Buscar Registro ")
    print("3. Eliminar Registro")
    print("4. Mostrar Registros")
    print("5. Salir")
    op = int(input("Digite tu opcion: "))
    return op

def main():
    op = 0
    while (op != 5):
        op = menu()
        if(op == 1): agregar()
        elif(op == 2): buscarRegistro()
        elif(op == 3): eliminarRegistro()
        elif(op == 4): mostrarRegistros()
        elif(op == 5): print("Adios...")
        

main()
