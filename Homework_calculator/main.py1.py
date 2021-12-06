
def print_welcome_message():
    print("Bienvenido a la CALCULADORA ")
    print("Esta en una calculadora de operacion basicas")
    print("que trabaja con operaciones de maximo dos valores")

def selection_menu():
    print("1.SUMA")
    print("2.RESTA")
    print("3.MULTIPLICACION")
    print("4.DIVISION")
    print("Ingrese una opcion del menu --> ")
    return int(input())

print_welcome_message()
option=selection_menu()

def numbers_selections1():
    print("Ingrese valor 1 --->")
    return int(input())

def numbers_selections2():
    print("Ingrese valor 2 --->")
    return int(input())

number_1 = numbers_selections1()
number_2 = numbers_selections2()

result=0.0

def option_sum(number_1,number_2):
    result = number_1 + number_2
    print("Resultado ---> ", result)


def option_rest(number_1,number_2):
    result= number_1 - number_2
    print("Resultado ---> ", result)

def option_multiplication(number_1,number_2):
    result = number_1 * number_2
    print("Resultado ---> ", result)

def option_division_(number_1,number_2):
    if number_2 == '0':
        print("Error matematico, la division no es posible ")
    else:
        result = number_1 / number_2
        print("Resultado ---> ", result)

if option == 1 :
    option_sum(number_1, number_2)

elif option == 2 :
    option_rest(number_1, number_2)

elif option == 3 :
    option_multiplication(number_1, number_2)

else :
    option_division_(number_1, number_2)

