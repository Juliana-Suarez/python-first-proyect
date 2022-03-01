def print_welcome_message():
    print("Bienvenido a la CALCULADORA ")
    print("Esta en una calculadora de operacion basicas")
    print("que trabaja con operaciones de maximo dos valores")

def selection_menu():
    print("1.SUMA")
    print("2.RESTA")
    print("3.MULTIPLICACION")
    print("4.DIVISION")
    print("5.SALIR")
    print("Ingrese una opcion del menu --> ")
    return int(input())
def Continue():
    print("'C' para continuar 'S' para salir")
    return str(input())

print_welcome_message()
var= Continue()

while var == 'C':

    option=selection_menu()

    def numbers_selections1():
        print("Ingrese valor 1 --->")
        return int(input())

    def numbers_selections2():
        print("Ingrese valor 2 --->")
        return int(input())

    result=0.0

    def option_sum():
        number_1 = numbers_selections1()
        number_2 = numbers_selections2()
        result = number_1 + number_2
        print("Resultado ---> ", result)


    def option_rest():
        number_1 = numbers_selections1()
        number_2 = numbers_selections2()
        result= number_1 - number_2
        print("Resultado ---> ", result)

    def option_multiplication():

        number_1 = numbers_selections1()
        number_2 = numbers_selections2()
        result = number_1 * number_2
        print("Resultado ---> ", result)

    def option_division_():
        number_1 = numbers_selections1()
        number_2 = numbers_selections2()
        if number_2 == '0':
            print("Error matematico, la division no es posible ")
        else:
            result = number_1 / number_2
            print("Resultado ---> ", result)

    if option == 1 :
        option_sum()

    elif option == 2 :
        option_rest()

    elif option == 3 :
        option_multiplication()

    elif option == 4 :
        option_division_()

    else :
        print ("Esta opcion no esta disponible")

    var = Continue()