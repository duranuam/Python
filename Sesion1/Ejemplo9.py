#Leer un num y generar la tabla de multiplicación
#de dicho numero.
num = int(input("Dime un #: "))
cont = 1
while(cont <= 12):
    result = num * cont
    print(f"{num} * {cont} = {result}")
    cont += 1 # cont = cont + 1
print("fin")