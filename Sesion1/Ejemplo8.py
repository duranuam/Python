#Leer el nombre y apellido de una persona
#a partir de esos datos generar un correo electrico
#uam

nombre = input("Nombre: ")
apellido = input("Apellido: ")
correo = f"{nombre.lower()}.{apellido.lower()}@uamv.edu.ni"
#correo = nombre +"."+apellido+"@uamv.edu.ni"
print(correo)
