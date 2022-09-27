#Leer dos numeros y decir quien es mayor, quien es menor o
#si ambos numeros son iguales
num1 = int(input("Dime el primer valor: "))
num2 = int(input("Dime el segundo valor: "))
if(num1 > num2):
    print("El mayor es ", num1)
    print("El menor es ", num2)
elif(num1 < num2):
    print("El mayor es", num2)
    print("El menor es", num1)
elif(num1 == num2):
   print("Ambos numero son iguales")

        