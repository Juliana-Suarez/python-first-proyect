import file_user

def correo():
    print("LOGIN")
    print("Ingrese su correo electronico")
    return str(input())

def contrasena():
    print("Ingrese su contraseña")
    return str(input())

usuario = correo()
password = contrasena()

def enunciado_de_verificacion(password,usuario):
    if not usuario.strip():
        print("No lleno el campo. Ingrese un correo\n")
    elif usuario.count("@") == 0:
        print("Ingrese un correo electronico\n")

    if 1 < password.count("") < 8:
        print("Contraseña corta / Minimo 8 caracteres\n ")
    elif not password.strip():
        print("No lleno el campo. Ingrese una contraseña\n")



def verificacion_basica(password,usuario):

    while not usuario.strip() or usuario.count("@")==0 or 1< password.count("")<8 or not password.strip():

        enunciado_de_verificacion(password,usuario)
        print("\n")
        usuario = correo()
        password = contrasena()


verificacion_basica(password,usuario)


real_password=file_user.password_1()
real_user=file_user.user_1()

real_password2 = file_user.password_2()
real_user2 = file_user.user_2()

while(usuario != real_user2 and password != real_password) or (usuario != real_user and password != real_password2)  :
    print("El e-mail o contraseña es incorrecta\nVuelva a intentarlo \n")
    usuario = correo()
    password = contrasena()
    verificacion_basica(password,usuario)

print("SESION INICIADA")
