print("Bienvenido a la CALCULADORA ")
print("Esta en una calculadora de operacion basicas")
print("que trabaja con operaciones de maximo dos valores")

print("1.SUMA")
print("2.RESTA")
print("3.MULTIPLICACION")
print("4.DIVISION")

opcion = input('Escoja la operacion que desea hacer: ')

if opcion == '1' :
    number_1 = int(input("Ingrese valor 1 --->"))
    number_2 = int(input("Ingrese valor 2 --->"))
    sum = number_1+number_2
    print("Resultado es ---> ", sum  )

elif opcion == '2' :
    number_1 = int(input("Ingrese valor 1 --->"))
    number_2 = int(input("Ingrese valor 2 --->"))
    rest = number_1 - number_2
    print("Resultado es ---> ", rest)

elif opcion == '3' :
    number_1 = int(input("Ingrese valor 1 --->"))
    number_2 = int(input("Ingrese valor 2 --->"))
    multiplication = number_1 * number_2
    print("Resultado es ---> ", multiplication)

else :
    number_1 = int(input("Ingrese valor 1 --->"))
    number_2 = int(input("Ingrese valor 2 --->"))
    if number_2 == '0':
        print("Error matematico, la division no es posible ")
    else:
        division = number_1 / number_2
        print("Resultado es ---> ", division)




